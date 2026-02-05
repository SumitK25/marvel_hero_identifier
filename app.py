import streamlit as st
import joblib
import pandas as pd
import plotly.graph_objects as go
import os

# Page config
st.set_page_config(
    page_title="Marvel Hero Identifier",
    page_icon="🦸",
    layout="wide"
)

# Load model and data
@st.cache_resource
def load_model():
    """Load the trained model, scaler, and data"""
    try:
        knn = joblib.load("model/knn_model.pkl")
        scaler = joblib.load("model/scaler.pkl")
        df = pd.read_csv("data/processed/marvel_heroes.csv")
        return knn, scaler, df
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None, None

knn, scaler, marvel_df = load_model()

# App title and description
st.title("🦸 Marvel Hero Identifier")
st.markdown("""
**Find your Marvel superhero match!** Enter your stats below and discover which Marvel heroes are most similar to you.
""")

if marvel_df is not None:
    STAT_COLUMNS = ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']
    
    # Sidebar for inputs
    st.sidebar.header("⚙️ Your Hero Stats")
    st.sidebar.markdown("Adjust the sliders to define your superhero stats (0-100)")
    
    user_stats = {}
    for stat in STAT_COLUMNS:
        user_stats[stat] = st.sidebar.slider(
            stat.capitalize(),
            min_value=0,
            max_value=100,
            value=50,
            help=f"Your {stat} level"
        )
    
    # Number of results
    k = st.sidebar.slider("Number of matches", min_value=1, max_value=10, value=5)
    
    # Main content
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📊 Your Stats")
        
        # Create radar chart
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=list(user_stats.values()),
            theta=[s.capitalize() for s in STAT_COLUMNS],
            fill='toself',
            name='Your Stats',
            line_color='#e63946'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )
            ),
            showlegend=False,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Display stats as metrics
        st.markdown("### Stats Summary")
        cols = st.columns(3)
        for idx, (stat, value) in enumerate(user_stats.items()):
            with cols[idx % 3]:
                st.metric(stat.capitalize(), value)
    
    with col2:
        st.subheader("🎯 Your Matches")
        
        if st.button("🔍 Find Similar Heroes", type="primary", use_container_width=True):
            # Get user stats as list
            stats_list = [user_stats[stat] for stat in STAT_COLUMNS]
            
            # Scale and predict
            stats_scaled = scaler.transform([stats_list])
            distances, indices = knn.kneighbors(stats_scaled, n_neighbors=k)
            
            # Display results
            st.markdown("### Top Matches:")
            
            for i, (idx, dist) in enumerate(zip(indices[0], distances[0]), 1):
                hero = marvel_df.iloc[idx]
                
                with st.container():
                    st.markdown(f"**#{i} - {hero['name']}**")
                    
                    # Progress bars for each stat
                    cols_stats = st.columns(len(STAT_COLUMNS))
                    for j, stat in enumerate(STAT_COLUMNS):
                        with cols_stats[j]:
                            st.caption(stat.capitalize()[:3])
                            st.progress(int(hero[stat]) / 100)
                    
                    st.caption(f"Match Score: {100 - min(dist * 10, 100):.1f}%")
                    st.divider()
    
    # Additional info
    st.markdown("---")
    st.markdown(f"**Database:** {len(marvel_df)} Marvel heroes | **Algorithm:** K-Nearest Neighbors")
    
    # Show random heroes for inspiration
    with st.expander("💡 Need inspiration? View random heroes"):
        random_heroes = marvel_df.sample(5)
        for _, hero in random_heroes.iterrows():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.markdown(f"**{hero['name']}**")
            with col2:
                stats_str = " | ".join([f"{stat.capitalize()[:3]}: {int(hero[stat])}" for stat in STAT_COLUMNS])
                st.caption(stats_str)
else:
    st.error("⚠️ Model files not found. Please train the model first.")
