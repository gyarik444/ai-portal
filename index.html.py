<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Portal — Всё про Искусственный Интеллект и Технологии</title>
    <style>
        :root {
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-color: #f8fafc;
            --text-muted: #94a3b8;
            --accent-color: #38bdf8;
            --accent-hover: #0ea5e9;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }

        header {
            background: var(--card-bg);
            padding: 1.5rem 2rem;
            border-bottom: 1px solid #334155;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--accent-color);
            text-decoration: none;
        }

        nav a {
            color: var(--text-muted);
            text-decoration: none;
            margin-left: 1.5rem;
            transition: color 0.2s;
        }

        nav a:hover {
            color: var(--accent-color);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem 1rem;
            flex: 1;
            width: 100%;
        }

        /* Рекламный блок */
        .ad-banner {
            background: #1e293b;
            border: 2px dashed #475569;
            color: var(--text-muted);
            text-align: center;
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            font-size: 0.9rem;
        }

        .hero {
            text-align: center;
            margin-bottom: 3rem;
        }

        .hero h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }

        .hero p {
            color: var(--text-muted);
            font-size: 1.1rem;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .card {
            background: var(--card-bg);
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid #334155;
            transition: transform 0.2s, border-color 0.2s;
            display: flex;
            flex-direction: column;
        }

        .card:hover {
            transform: translateY(-4px);
            border-color: var(--accent-color);
        }

        .card-content {
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
            flex: 1;
        }

        .card h3 {
            font-size: 1.25rem;
            margin-bottom: 0.75rem;
        }

        .card p {
            color: var(--text-muted);
            font-size: 0.95rem;
            margin-bottom: 1.5rem;
            flex: 1;
        }

        .btn {
            display: inline-block;
            background: var(--accent-color);
            color: #0f172a;
            padding: 0.6rem 1.2rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            text-align: center;
            transition: background 0.2s;
        }

        .btn:hover {
            background: var(--accent-hover);
        }

        footer {
            background: var(--card-bg);
            border-top: 1px solid #334155;
            text-align: center;
            padding: 1.5rem;
            color: var(--text-muted);
            font-size: 0.9rem;
            margin-top: auto;
        }

        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>

    <header>
        <a href="#" class="logo">⚡ AI Portal</a>
        <nav>
            <a href="#">Главная</a>
            <a href="#">Статьи</a>
            <a href="#">Инструменты</a>
            <a href="#">Контакты</a>
        </nav>
    </header>

    <div class="container">
        
        <!-- Рекламный блок в шапке (сюда вставляется код баннера) -->
        <div class="ad-banner">
            📢 Место под вашу рекламу / Рекламный баннер (Google AdSense / РСЯ)
        </div>

        <section class="hero">
            <h1>Будущее уже здесь</h1>
            <p>Узнайте, как использовать искусственный интеллект для работы, учебы и повседневных задач.</p>
        </section>

        <div class="grid">
            <div class="card">
                <div class="card-content">
                    <h3>Топ-5 нейросетей для создания текстов</h3>
                    <p>Подробный разбор лучших инструментов, которые помогут написать статью, пост или курсовую за пару минут.</p>
                    <a href="#" class="btn">Читать статью</a>
                </div>
            </div>

            <div class="card">
                <div class="card-content">
                    <h3>Как генерировать крутые картинки по тексту</h3>
                    <p>Секреты составления промптов (запросов) для Midjourney и Stable Diffusion для получения идеального результата.</p>
                    <a href="#" class="btn">Читать статью</a>
                </div>
            </div>

            <div class="card">
                <div class="card-content">
                    <h3>Автоматизация рутины с помощью ИИ</h3>
                    <p>Как настроить умных ассистентов, чтобы они выполняли за вас скучные рутинные задачи на компьютере.</p>
                    <a href="#" class="btn">Читать статью</a>
                </div>
            </div>
        </div>

        <!-- Еще один рекламный блок посреди контента -->
        <div class="ad-banner" style="margin-top: 2rem;">
            📢 Рекламный блок в ленте материалов
        </div>

    </div>

    <footer>
        <p>&copy; 2026 AI Portal. Все права защищены.</p>
    </footer>

</body>
</html>