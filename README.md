# 🦸 Marvel Hero Identifier

Find your Marvel superhero match using K-Nearest Neighbors machine learning!

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![Marvel Hero Identifier Demo](https://via.placeholder.com/800x400.png?text=Marvel+Hero+Identifier)

## 🌟 Features

- **Interactive Web Interface**: Easy-to-use sliders for defining your hero stats
- **Visual Radar Chart**: See your stats visualized in real-time
- **Top Matches**: Find the most similar Marvel heroes using KNN algorithm
- **Match Score**: See percentage similarity with each hero
- **Hero Database**: 100+ Marvel superheroes with complete stats

## 🎮 Live Demo

Try it out: [Marvel Hero Identifier](https://your-app-url.streamlit.app) *(Coming soon)*

## 📊 How It Works

The application uses a **K-Nearest Neighbors (KNN)** machine learning algorithm trained on Marvel superhero data. It compares your custom stats across 6 key dimensions:

| Stat | Description |
|------|-------------|
| 🧠 **Intelligence** | Mental capacity and problem-solving |
| 💪 **Strength** | Physical power |
| ⚡ **Speed** | Movement and reflexes |
| 🛡️ **Durability** | Ability to withstand damage |
| ✨ **Power** | Special abilities and energy manipulation |
| ⚔️ **Combat** | Fighting skills and tactics |

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/SumitK25/marvel_hero_identifier.git
cd marvel_hero_identifier
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Open your browser**
   - Navigate to `http://localhost:8501`
   - Start finding your Marvel match! 🎉

## 📁 Project Structure
```
marvel_hero_identifier/
├── app.py                      # Main Streamlit application
├── data/
│   ├── raw/                    # Original superhero dataset
│   │   └── heroes_information.csv
│   └── processed/              # Cleaned Marvel heroes data
│       └── marvel_heroes.csv
├── model/
│   ├── knn_model.pkl          # Trained KNN model
│   └── scaler.pkl             # Feature scaler
├── requirements.txt           # Python dependencies
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## 🎯 Usage

1. **Adjust Your Stats**: Use the sliders in the sidebar to set your superhero attributes (0-100)
2. **Visualize**: See your stats displayed in an interactive radar chart
3. **Find Matches**: Click "Find Similar Heroes" button
4. **Explore Results**: View your top matching Marvel heroes with similarity scores

## 🚀 Deployment

### Deploy to Streamlit Cloud (Free & Easy)

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Select your forked repository
5. Set main file path: `app.py`
6. Click "Deploy"

Your app will be live in 2-3 minutes! ✨

### Deploy to Heroku

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed Heroku deployment instructions.

## 🛠️ Technical Details

### Machine Learning Model

- **Algorithm**: K-Nearest Neighbors (KNN)
- **Distance Metric**: Euclidean distance
- **Features**: 6 numerical stats per hero
- **Preprocessing**: StandardScaler for feature normalization
- **Training Data**: Marvel Comics superheroes

### Tech Stack

- **Frontend**: Streamlit
- **ML Library**: scikit-learn
- **Data Processing**: pandas, numpy
- **Visualization**: plotly
- **Model Serialization**: joblib

## 📊 Dataset

The dataset includes Marvel superheroes with the following attributes:
- Hero name
- 6 combat statistics (intelligence, strength, speed, durability, power, combat)
- Publisher information

Data source: [Superhero API](https://superheroapi.com/)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 To-Do

- [ ] Add DC Comics heroes
- [ ] Include hero images
- [ ] Add comparison feature between two heroes
- [ ] Export results as PDF
- [ ] Add hero backstory information
- [ ] Mobile responsive improvements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Marvel Comics for the amazing superheroes
- [Superhero API](https://superheroapi.com/) for the dataset
- [Streamlit](https://streamlit.io/) for the amazing framework
- The open-source community

## 📧 Contact

**Sumit Kumar**
- GitHub: [@SumitK25](https://github.com/SumitK25)
- Project Link: [https://github.com/SumitK25/marvel_hero_identifier](https://github.com/SumitK25/marvel_hero_identifier)

---

⭐ **Star this repo** if you found it helpful!

Made with ❤️ for Marvel fans
