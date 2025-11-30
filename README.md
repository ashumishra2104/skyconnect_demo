# ✈️ SkyConnect - Flight Booking Application

SkyConnect is a modern, premium flight booking application built with **Streamlit**. It offers a seamless user experience for searching flights, selecting seats, managing add-ons, and processing payments, all wrapped in a beautiful, responsive UI.

## ✨ Features

-   **Flight Search**: Search for flights between major cities with real-time-like filtering.
-   **Premium UI**: Custom CSS theme with glassmorphism, gradients, and modern typography (Inter & Outfit fonts).
-   **Interactive Seat Map**: Visual seat selection with dynamic pricing based on seat type.
-   **Add-ons**: Manage baggage, meals, and insurance options.
-   **AI Assistant**: Integrated chatbot (powered by n8n) for instant customer support.
-   **Payment Simulation**: Secure-looking payment processing flow.

## 🛠️ Tech Stack

-   **Frontend/Backend**: Python, Streamlit
-   **Styling**: Custom CSS3, Google Fonts
-   **Chatbot**: n8n (Webhook integration)
-   **Database**: PostgreSQL (Integration ready)

## 🚀 Getting Started

### Prerequisites

-   Python 3.8+
-   pip

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/ashumishra2104/skyconnect_demo.git
    cd skyconnect_demo
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Run the application:
    ```bash
    streamlit run app.py
    ```

4.  Open your browser at `http://localhost:8501`.

## 📂 Project Structure

```
SkyConnect/
├── app.py                  # Main application entry point
├── assets/
│   └── style.css           # Premium custom CSS styles
├── components/
│   ├── search.py           # Flight search component
│   ├── results.py          # Flight results display
│   ├── details.py          # Passenger details form
│   ├── seats.py            # Interactive seat map
│   ├── addons.py           # Baggage and meal selection
│   ├── payment.py          # Payment processing
│   └── chatbot.py          # AI Chatbot integration
├── utils/
│   └── session.py          # Session state management
└── requirements.txt        # Project dependencies
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.
