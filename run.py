import os

if __name__ == '__main__':
    try:
        os.system("streamlit run .\\1_🏠_HOME.py")
    except KeyboardInterrupt:
        exit()
    except Exception:
        print("closed")
        exit()
