import streamlit as st
import cv2
import csv
from PIL import Image
import pandas as pd
import time
from datetime import datetime


# To display the webcam feed
FRAME_WINDOW = st.image([])

def run_app():
    # sidebar
    st.sidebar.image("../../assets/logo.png")
    st.sidebar.header("Log maker")
    st.sidebar.subheader(
        "An interactive logging application to upload/connect camera to start the captioning and save the captions in an encrypted form for added secuirity."
    )

    # source selector
    st.header("Select the source of the feed:")
    source = st.selectbox("", ("Live Camera", "Upload"))

    if source == "Upload":
        video_file = st.file_uploader("surveillance feed", accept_multiple_files=False, type=['mp4'])
        tfile = tempfile.NamedTemporaryFile(delete=False)
        if video_file is not None:
            tfile.write(video_file.read())
        vid = cv2.VideoCapture(tfile.name)
    if source == "Live Camera":   
        vid = cv2.VideoCapture(0)
    run = st.checkbox("Run", key="start")
    show_frame = st.checkbox("Show frames", key="frame")
    csvw = CSVWorker()
    # Starts the app, when the button is clicked    
    while(run):
        _, frame = vid.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if(show_frame):
            FRAME_WINDOW.image(frame)
        img = Image.fromarray(frame)
        img = img.resize((224, 224))
        pred = test(img)
        csvw.write(pred)
        st.write(pred)
        time.sleep(5)
    vid.release()
    cv2.destroyAllWindows()


def main():
    run_app()
    # trial()


@st.cache(show_spinner=False)
class CSVWorker:
    def __init__(self):
        self.fields = [
            "w1",
            "w2",
            "w3",
            "w4",
            "w5",
            "w6",
            "w7",
            "w8",
            "w9",
            "w10",
            "time",
            "camera",
        ]
        self.filename = "results.csv"
        self.create_csv()

    def preprocess(self, text, tokenizer):
        sequences = tokenizer.texts_to_sequences(text)
        return sequences

    def create_csv(self):
        df = pd.DataFrame(list(), columns=self.fields)
        df.to_csv(self.filename)

    def write(self, pred):
        df = pd.read_csv(self.filename)
        # pred = self.preprocess(pred, TOKENIZER)
        pred = pred.split(" ")
        if len(pred) >= 10:
            entry = [
                pred[0],
                pred[1],
                pred[2],
                pred[3],
                pred[4],
                pred[5],
                pred[6],
                pred[7],
                pred[8],
                pred[9],
                datetime.now(),
                1,
            ]
        elif len(pred) < 10:
            entry = []
            for i in range(len(pred)):
                entry.append(pred[i])
            for i in range(len(entry) - 1, 11):
                entry.append("")
            entry.append(datetime.now)
            entry.append(1)
        with open(self.filename, "a") as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # writing data rows
            csvwriter.writerow(entry)


if __name__ == "__main__":
    main()
