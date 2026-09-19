<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Email Subject Line Encoder</title>
  <style>
    body { font-family: sans-serif; padding: 20px; max-width: 600px; }
    textarea, input, select, button { width: 100%; margin-bottom: 12px; padding: 8px; }
    .output { background: #f4f4f4; padding: 10px; word-break: break-all; font-family: monospace; }
  </style>
</head>
<body>

  <h2>Email Subject Encoder</h2>

  <label>Subject Line Input:</label>
  <input type="text" id="subjectInput" placeholder="Enter subject line...">

  <label>Character Set:</label>
  <select id="charset">
    <option value="UTF-8">UTF-8</option>
    <option value="GB2312">GB2312</option>
    <option value="ISO-8859-1">ISO-8859-1</option>
  </select>

  <button onclick="generateEncoding()">Generate Variations</button>

  <h3>Outputs:</h3>
  <p><strong>Base64 (B):</strong></p>
  <div id="base64Output" class="output"></div>

  <p><strong>Quoted-Printable (Q) with Noise:</strong></p>
  <div id="qpOutput" class="output"></div>

  <script>
    // Noise characters (Zero-width spaces, joiners, soft hyphens)
    const NOISE_BYTES = ['\u200B', '\u200C', '\u200D', '\u00AD', '\uFEFF'];

    function injectNoise(text) {
      return text.split('').map(char => {
        // Randomly insert a noise byte after characters
        if (Math.random() > 0.6) {
          const randomNoise = NOISE_BYTES[Math.floor(Math.random() * NOISE_BYTES.length)];
          return char + randomNoise;
        }
        return char;
      }).join('');
    }

    function encodeQuotedPrintable(text) {
      return text.split('').map(c => {
        const code = c.charCodeAt(0);
        // Convert non-alphanumeric chars to hex format =XX
        if ((code >= 48 && code <= 57) || (code >= 65 && code <= 90) || (code >= 97 && code <= 122)) {
          return c;
        }
        return '=' + code.toString(16).toUpperCase().padStart(2, '0');
      }).join('');
    }

    function generateEncoding() {
      const input = document.getElementById('subjectInput').value;
      const charset = document.getElementById('charset').value;

      if (!input) return;

      // 1. Base64 Encoding
      const b64 = btoa(unescape(encodeURIComponent(input)));
      document.getElementById('base64Output').innerText = `=?${charset}?B?${b64}?=`;

      // 2. Quoted-Printable with Noise Injection
      const noisyText = injectNoise(input);
      const qp = encodeQuotedPrintable(noisyText);
      document.getElementById('qpOutput').innerText = `=?${charset}?Q?${qp}?=`;
    }
  </script>
</body>
</html>
