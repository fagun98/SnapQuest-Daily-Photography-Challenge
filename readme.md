# SnapQuest: Daily Photography Challenge

SnapQuest is a fun and interactive daily photography challenge app built using Streamlit. Every day at 10 AM UTC, a new object is revealed, challenging users to capture creative photos and submit them to the gallery. Whether you're a seasoned photographer or just getting started, SnapQuest helps you improve your skills and explore the world around you in a new light.

![SnapQuest Banner](https://images.unsplash.com/photo-1517336714731-489689fd1ca8)

## Features

- **Daily Object Challenge:** Each day, a new object is randomly selected for users to photograph.
- **Live Countdown:** A real-time timer shows the time remaining until the next object is revealed.
- **Photo Uploads:** Users can upload their photos directly through the app.
- **Gallery:** View photos uploaded by others in a Pinterest-style gallery.
- **Rules & Tips:** Learn photography techniques to enhance your photos and capture the daily challenge in the best light.

## How It Works

1. **Daily Object:** SnapQuest reveals a new object at 10 AM UTC every day.
2. **Upload Photos:** Capture a photo of the object and upload it to the platform.
3. **Explore:** Check out the gallery to see how others have captured the same object.
4. **Countdown Timer:** Track the time left until the next daily object reset.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/SnapQuest-Daily-Photography-Challenge.git
    cd SnapQuest-Daily-Photography-Challenge
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `secrets.toml` file in the `.streamlit/` directory:

    ```toml
    [constants]
    reset_hour = 10  # Set the hour for daily reset (in UTC)
    upload_dir = "uploads"
    today_object_dir = "uploads/today"
    objects = ["Tree", "Bicycle", "Lamp Post", "Street Art", "Bird", "Flower", "Cloud", ...]
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## How to Play

1. Visit the **Today's Challenge** tab to view the daily object.
2. Upload your best photo of the object.
3. Explore the **Gallery** to view submissions from other players.
4. Check out the **Rules & Tips** for helpful photography advice.

## Technologies Used

- **Streamlit:** Frontend framework for building interactive data applications.
- **PIL (Pillow):** Image processing and handling for uploaded photos.
- **Python:** Backend logic for handling objects, gallery resets, and more.

## Contributing

We welcome contributions! Here's how you can get started:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes and push them to GitHub.
4. Create a pull request.

## Contact

For any inquiries or feedback, please reach out via email: fagun.raithatha28@gmail.com

---

Enjoy your photography adventure with SnapQuest!