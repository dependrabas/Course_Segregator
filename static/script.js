// DOM Elements
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const processBtn = document.getElementById('processBtn');
const clearBtn = document.getElementById('clearBtn');
const fileInfo = document.getElementById('fileInfo');
const fileName = document.getElementById('fileName');
const fileSize = document.getElementById('fileSize');
const statusSection = document.getElementById('statusSection');
const outputCard = document.getElementById('outputCard');
const outputContent = document.getElementById('outputContent');
const filesCard = document.getElementById('filesCard');
const filesList = document.getElementById('filesList');

let selectedFile = null;

// Upload Area Click
uploadArea.addEventListener('click', () => fileInput.click());

// File Input Change
fileInput.addEventListener('change', (e) => {
    handleFileSelect(e.target.files[0]);
});

// Drag and Drop
uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.classList.add('dragover');
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('dragover');
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.classList.remove('dragover');
    handleFileSelect(e.dataTransfer.files[0]);
});

// Handle File Selection
function handleFileSelect(file) {
    if (!file) return;

    if (!file.name.endsWith('.csv')) {
        showError('Please select a CSV file');
        return;
    }

    selectedFile = file;
    fileName.textContent = `✓ ${file.name}`;
    fileSize.textContent = `(${(file.size / 1024).toFixed(1)} KB)`;
    fileInfo.style.display = 'flex';
    processBtn.disabled = false;
}

// Process File
processBtn.addEventListener('click', async () => {
    if (!selectedFile) return;

    const formData = new FormData();
    formData.append('file', selectedFile);

    statusSection.style.display = 'block';
    outputCard.style.display = 'none';
    processBtn.disabled = true;

    try {
        const response = await fetch('/api/upload', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (!data.success) {
            showError(data.error || 'Error processing file');
            statusSection.style.display = 'none';
            processBtn.disabled = false;
            return;
        }

        // Display results
        displayResults(data);
        loadFiles();
        statusSection.style.display = 'none';
        outputCard.style.display = 'block';
        filesCard.style.display = 'block';

    } catch (error) {
        showError('Error uploading file: ' + error.message);
        statusSection.style.display = 'none';
        processBtn.disabled = false;
    }
});

// Display Results
function displayResults(data) {
    let html = `<p class="success-message">✓ Success! Processing completed.</p>`;
    html += `<p>CSV files created (${data.files_created} file(s)):</p>`;
    html += '<div style="margin-top: 10px;">';

    data.files.forEach((file, index) => {
        html += `<div class="file-item">${index + 1}. ${file.name}</div>`;
    });

    html += '</div>';
    outputContent.innerHTML = html;
}

// Load Files List
async function loadFiles() {
    try {
        const response = await fetch('/api/files');
        const data = await response.json();

        if (data.files.length === 0) {
            filesList.innerHTML = '<p style="color: #95a5a6;">No files generated yet</p>';
            return;
        }

        let html = '';
        data.files.forEach(file => {
            html += `
                <div class="file-row">
                    <div class="file-info-text">
                        <span class="file-name">${file.name}</span>
                        <span class="file-size">${file.size}</span>
                    </div>
                    <a href="/api/download/${file.filename}" class="btn-download">
                        ⬇️ Download
                    </a>
                </div>
            `;
        });

        filesList.innerHTML = html;

    } catch (error) {
        console.error('Error loading files:', error);
    }
}

// Clear
clearBtn.addEventListener('click', () => {
    selectedFile = null;
    fileInput.value = '';
    fileInfo.style.display = 'none';
    processBtn.disabled = true;
    outputCard.style.display = 'none';
    statusSection.style.display = 'none';
});

// Show Error
function showError(message) {
    outputCard.style.display = 'block';
    outputContent.innerHTML = `<div class="error-message">⚠️ ${message}</div>`;
}

// Load files on page load
loadFiles();
