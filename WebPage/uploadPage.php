<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="uploadPage.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link href='https://fonts.googleapis.com/css?family=ABeeZee' rel='stylesheet'>
    <link href='https://fonts.googleapis.com/css?family=B612' rel='stylesheet'>
    <script>
        function autoSubmit() {
            document.getElementById("uploadForm").submit();
        }
    </script>
    <title>Tagalog Transcription</title>
</head>
<body>
    <nav class="nav">
        <a class="mainPageLink" href="mainPage.php">Tagalog Transcription</a>
    </nav>
    
    <div class="controller">
        <div class="btnUpload">
            <div class="bg">
            <form id="uploadForm" action="uploadFunction.php" method="post" enctype="multipart/form-data">
                <input id="fileInput" type="file" name="audioFile" accept="audio/*" onchange="autoSubmit()" required>
                <label for="fileInput">Upload File</label>
            </form>
            </div>
        </div>
        <br>
        <hr>
        <br>
        <div class="btnDownload">
            <a href="uploadPage.php" class="btn" action="uploadFunction.php">Download</a>
        </div>
    </div>
</body>
</html>
