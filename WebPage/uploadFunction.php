<?php
// folder name
$audioFolder = 'audioFile';
$txtFolder = 'txtFile';

// Create audioFile folder (prevent recreate)
if (!file_exists($audioFolder)) {
    mkdir($audioFolder, 0777, true);
}
if (!file_exists($txtFolder)) {
    mkdir($txtFolder, 0777, true);
}

// Check if a file is uploaded
if (isset($_FILES['audioFile']) && $_FILES['audioFile']['error'] == 0) {
    // Get the file details
    $fileName = $_FILES['audioFile']['name'];
    $fileTmpName = $_FILES['audioFile']['tmp_name'];
    
    // Define the target file path in the audioFile folder
    $targetFilePath = $audioFolder . '/' . $fileName;

    // Move the uploaded file to the audioFile folder
    if (move_uploaded_file($fileTmpName, $targetFilePath)) {
        // Show alert for success and stay on the same page
        echo "<script type='text/javascript'>alert('File uploaded successfully!');
        window.history.back();
        </script>";
    } else {
        // Show alert for error and stay on the same page
        echo "<script type='text/javascript'>alert('There was an error uploading your file.');
        window.history.back();
        </script>";
    }
} else {
    // Show alert if no file is uploaded and stay on the same page
    echo "<script type='text/javascript'>alert('No file uploaded or there was an upload error.');
    window.history.back();
    </script>";
}
?>
