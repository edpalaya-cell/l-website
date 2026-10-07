from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>For My Love ❤️</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            height: 100vh;
            overflow: hidden;
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
            font-family: 'Segoe UI', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }
        .message {
            text-align: center;
            z-index: 10;
            color: #fff;
            text-shadow: 0 0 20px rgba(255, 0, 100, 0.8), 0 0 40px rgba(255, 0, 100, 0.5);
            animation: pulse 2s infinite;
        }
        .message h1 { font-size: 3.5rem; margin-bottom: 15px; }
        .message p { font-size: 1.5rem; }
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        .heart {
            position: absolute;
            width: 28px; height: 28px;
            background: #ff2e63;
            transform: rotate(45deg);
            animation: floatUp linear infinite;
            opacity: 0.85;
            z-index: 1;
        }
        .heart::before, .heart::after {
            content: '';
            position: absolute;
            width: 28px; height: 28px;
            background: #ff2e63;
            border-radius: 50%;
        }
        .heart::before { top: -14px; left: 0; }
        .heart::after { left: -14px; top: 0; }
        @keyframes floatUp {
            0% { transform: translateY(100vh) rotate(45deg) scale(0.5); opacity: 0; }
            20% { opacity: 0.9; }
            100% { transform: translateY(-80px) rotate(45deg) scale(1.2); opacity: 0; }
        }
        .balloon {
            position: absolute;
            width: 55px; height: 65px;
            border-radius: 50% 50% 50% 50% / 40% 40% 60% 60%;
            animation: rise linear infinite;
            z-index: 2;
        }
        .balloon::after {
            content: '';
            position: absolute;
            bottom: -18px;
            left: 50%;
            transform: translateX(-50%);
            width: 2px; height: 35px;
            background: rgba(0,0,0,0.3);
        }
        @keyframes rise {
            0% { transform: translateY(100vh) scale(0.8); opacity: 0; }
            10% { opacity: 1; }
            100% { transform: translateY(-120px) scale(1.1); opacity: 0; }
        }
        .firework {
            position: absolute;
            width: 6px; height: 6px;
            border-radius: 50%;
            animation: explode 1.4s ease-out infinite;
            z-index: 3;
        }
        @keyframes explode {
            0% { transform: scale(1); opacity: 1; box-shadow: 0 0 0 0 currentColor; }
            100% { transform: scale(22); opacity: 0; box-shadow: 0 0 35px 18px transparent; }
        }
        .sparkle {
            position: absolute;
            width: 7px; height: 7px;
            background: #fff;
            border-radius: 50%;
            animation: sparkle 2s linear infinite;
            z-index: 4;
        }
        @keyframes sparkle {
            0%, 100% { opacity: 0; transform: scale(0); }
            50% { opacity: 1; transform: scale(1.4); }
        }
    </style>
</head>
<body>
    <div class="message">
        <h1>I Love You ❤️</h1>
        <p>You make my heart float like these balloons</p>
        <p style="margin-top: 12px; font-size: 1.3rem;">Forever & Always 💕</p>
    </div>

    <script>
        function createHeart() {
            const heart = document.createElement('div');
            heart.classList.add('heart');
            heart.style.left = Math.random() * 100 + 'vw';
            heart.style.animationDuration = (Math.random() * 4 + 4) + 's';
            document.body.appendChild(heart);
            setTimeout(() => heart.remove(), 8000);
        }
        function createBalloon() {
            const balloon = document.createElement('div');
            balloon.classList.add('balloon');
            const colors = ['#ff6b6b', '#ff9ff3', '#feca57', '#48dbfb', '#ff6b81', '#a29bfe'];
            balloon.style.background = colors[Math.floor(Math.random() * colors.length)];
            balloon.style.left = Math.random() * 100 + 'vw';
            balloon.style.animationDuration = (Math.random() * 6 + 6) + 's';
            document.body.appendChild(balloon);
            setTimeout(() => balloon.remove(), 12000);
        }
        function createFirework() {
            const firework = document.createElement('div');
            firework.classList.add('firework');
            const colors = ['#ff2e63', '#ff9a00', '#00d2ff', '#ff00aa', '#ffff00', '#00ff88'];
            const color = colors[Math.floor(Math.random() * colors.length)];
            firework.style.background = color;
            firework.style.color = color;
            firework.style.left = Math.random() * 100 + 'vw';
            firework.style.top = Math.random() * 55 + 15 + 'vh';
            document.body.appendChild(firework);
            setTimeout(() => firework.remove(), 1400);
        }
        function createSparkle() {
            const sparkle = document.createElement('div');
            sparkle.classList.add('sparkle');
            sparkle.style.left = Math.random() * 100 + 'vw';
            sparkle.style.top = Math.random() * 100 + 'vh';
            document.body.appendChild(sparkle);
            setTimeout(() => sparkle.remove(), 2000);
        }

        setInterval(createHeart, 400);
        setInterval(createBalloon, 800);
        setInterval(createFirework, 550);
        setInterval(createSparkle, 280);

        for (let i = 0; i < 12; i++) {
            setTimeout(createHeart, i * 90);
            setTimeout(createBalloon, i * 140);
            setTimeout(createFirework, i * 70);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)