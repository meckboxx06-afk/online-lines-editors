
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Online Line Editor</title>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #10141c;
    color: white;
}

.header {
    background: #1c2330;
    padding: 15px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
}

.header h2 {
    margin: 0;
    color: #61dafb;
}

.buttons button {
    padding: 8px 12px;
    margin: 3px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    background: #2563eb;
    color: white;
}

.buttons button:hover {
    background: #1d4ed8;
}

.editor-container {
    display: flex;
    width: 100%;
    height: calc(100vh - 75px);
    overflow: hidden;
    background: #0d1117;
}

.line-numbers {
    width: 55px;
    padding: 15px 8px;
    text-align: right;
    color: #6b7280;
    background: #161b22;
    border-right: 1px solid #30363d;
    font-family: monospace;
    font-size: 15px;
    line-height: 1.6;
    white-space: pre;
    overflow: hidden;
    user-select: none;
}

#editor {
    flex: 1;
    padding: 15px;
    border: none;
    outline: none;
    resize: none;
    background: #0d1117;
    color: #e6edf3;
    font-family: monospace;
    font-size: 15px;
    line-height: 1.6;
    white-space: pre;
    overflow: auto;
    tab-size: 4;
}

</style>
</head>

<body>

<div class="header">

    <h2>Online Line Editor</h2>

    <div class="buttons">
        <button onclick="copyText()">Copy</button>
        <button onclick="downloadText()">Download</button>
        <button onclick="clearText()">Clear</button>
    </div>

</div>

<div class="editor-container">

    <div id="lineNumbers" class="line-numbers">1</div>

    <textarea
        id="editor"
        spellcheck="false"
        placeholder="Start typing your content here..."
    ></textarea>

</div>

<script>

const editor = document.getElementById("editor");
const lineNumbers = document.getElementById("lineNumbers");

function updateLineNumbers() {

    const lines = editor.value.split("\n").length;

    let numbers = "";

    for (let i = 1; i <= lines; i++) {
        numbers += i + "\n";
    }

    lineNumbers.textContent = numbers;

}

editor.addEventListener("input", updateLineNumbers);

editor.addEventListener("scroll", () => {

    lineNumbers.scrollTop = editor.scrollTop;

});

async function copyText() {

    try {
        await navigator.clipboard.writeText(editor.value);
        alert("Text copied successfully!");
    } catch (error) {
        alert("Unable to copy text.");
    }

}

function downloadText() {

    const blob = new Blob([editor.value], {
        type: "text/plain"
    });

    const link = document.createElement("a");

    link.href = URL.createObjectURL(blob);
    link.download = "my-editor-text.txt";

    link.click();

    URL.revokeObjectURL(link.href);

}

function clearText() {

    if (confirm("Are you sure you want to clear the editor?")) {

        editor.value = "";
        updateLineNumbers();

    }

}

updateLineNumbers();

</script>

</body>
</html>
