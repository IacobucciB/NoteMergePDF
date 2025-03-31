# NoteMergePDF

NoteMergePDF is a Python-based desktop application for merging and managing PDF files. It provides an intuitive graphical user interface (GUI) for selecting, reordering, splitting, and merging PDF files or specific pages. This tool is ideal for students, professionals, and anyone who frequently works with PDF documents.

## Features

- **Merge PDFs**: Combine multiple PDF files into a single document.
- **Split PDFs**: Extract individual pages from PDF files.
- **Reorder Files**: Easily reorder selected PDF files before merging.
- **Page Selection**: Select specific pages from multiple PDFs and merge them into a new document.
- **User-Friendly Interface**: Built with Tkinter for a clean and responsive GUI.

## Installation and Usage

### For Developers

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/IacobucciB/NoteMergePDF
   cd NoteMergePDF
   ```

2. **Install the Required Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   python main.py
   ```

### For End Users (Release Executable)

The release package includes an executable file generated using PyInstaller. Note that the executable is designed to pick up PDF files only from the **current folder** where it is run.

1. **Extract the Release Package:**
   - Unzip the release package (e.g., `NoteMergePDF_v1.0.Y.zip`) to your desired folder.

2. **Place Your PDF Files:**
   - Move or copy the PDF files you wish to work with into the same folder where the executable is located.

3. **Run the Executable:**
   - Double-click the executable file (e.g., `NoteMergePDF.exe`) to launch the application.
   - The application will automatically list any PDF files found in the current folder.
   - Use the **Select Files** button if needed, but note that the executable searches for PDF files only in the current folder.

4. **Application Workflow:**
   - **Reorder Files:** Use the **Up** and **Down** buttons to change the order of PDF files.
   - **Split PDFs:** Use the **Split** button to break PDFs into individual pages, which are displayed in the right panel.
   - **Merge Files/Pages:** Use the **Merge** button to combine the selected files or pages into a new PDF.
   - **Save the Output:** Choose the location to save the merged PDF document.

## Screenshots

![Main Interface](NoteMergePDF.png)  
*Screenshot of the application's main interface.*

## Logging

The application logs all operations (e.g., file selection, merging, splitting) to help with debugging and tracking actions. Logs are displayed in the console.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your fork:
   ```bash
   git commit -m "Add feature-name"
   git push origin feature-name
   ```
4. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


