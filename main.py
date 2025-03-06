import sys
from Content import Content
import streamlit as st

if __name__ == "__main__":
    
     try:
          content = Content(sys.argv[1])
          print(content.get_text())
          st.write(content.get_text())
     except():
          print("Please provide a file path")
          st.write("Please provide a file path")
    
    

    
