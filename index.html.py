<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cash Faster - أفضل وأسرع قرض في مصر</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #D32F2F;
            --primary-dark: #b71c1c;
            --secondary: #FFC107;
            --secondary-dark: #FFA000;
            --dark: #1a1a1a;
            --light: #ffffff;
            --gray: #f5f5f5;
            --text: #333333;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #000000 0%, #1a1a1a 100%);
            color: var(--light);
            min-height: 100vh;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 15px;
        }
        
        /* الشريط العلوي المتحرك */
        .top-ticker {
            background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%);
            padding: 10px 0;
            overflow: hidden;
            position: relative;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        }
        
        .ticker-content {
            display: inline-block;
            white-space: nowrap;
            animation: ticker-scroll 30s linear infinite;
            padding-right: 100%;
        }
        
        @keyframes ticker-scroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-100%); }
        }
        
        .ticker-item {
            display: inline-block;
            margin: 0 20px;
            font-weight: bold;
            font-size: 16px;
        }
        
        /* الهيدر */
        header {
            background: rgba(0, 0, 0, 0.8);
            padding: 20px 0;
            border-bottom: 2px solid var(--primary);
        }
        
        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            display: flex;
            align-items: center;
        }
        
        .logo-text {
            font-size: 28px;
            font-weight: bold;
            color: var(--light);
            text-shadow: 0 0 10px var(--primary), 0 0 20px var(--primary);
            animation: glow 2s infinite alternate;
        }
        
        @keyframes glow {
            from { text-shadow: 0 0 10px var(--primary), 0 0 20px var(--primary); }
            to { text-shadow: 0 0 15px var(--primary), 0 0 30px var(--primary), 0 0 40px var(--secondary); }
        }
        
        .logo-icon {
            font-size: 32px;
            color: var(--secondary);
            margin-left: 10px;
            animation: pulse 1.5s infinite alternate;
        }
        
        @keyframes pulse {
            from { transform: scale(1); }
            to { transform: scale(1.1); }
        }
        
        /* قسم البطل */
        .hero {
            padding: 60px 0;
            text-align: center;
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="%23D32F2F" fill-opacity="0.2" d="M0,128L48,117.3C96,107,192,85,288,112C384,139,480,213,576,218.7C672,224,768,160,864,138.7C960,117,1056,139,1152,149.3C1248,160,1344,160,1392,160L1440,160L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path></svg>') bottom no-repeat, linear-gradient(135deg, #000000 0%, #1a1a1a 100%);
            background-size: 100% 30%, cover;
        }
        
        .hero h1 {
            font-size: 42px;
            margin-bottom: 20px;
            color: var(--light);
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
        }
        
        .hero p {
            font-size: 20px;
            max-width: 800px;
            margin: 0 auto 30px;
            color: var(--light);
        }
        
        .highlight {
            color: var(--secondary);
            font-weight: bold;
        }
        
        /* أزرار مضيئة متحركة */
        .btn {
            display: inline-block;
            padding: 15px 30px;
            background: var(--primary);
            color: var(--light);
            border: none;
            border-radius: 50px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(211, 47, 47, 0.4);
            margin: 10px;
            position: relative;
            overflow: hidden;
            animation: pulse-btn 2s infinite;
        }
        
        @keyframes pulse-btn {
            0% { box-shadow: 0 0 0 0 rgba(211, 47, 47, 0.7); }
            70% { box-shadow: 0 0 0 15px rgba(211, 47, 47, 0); }
            100% { box-shadow: 0 0 0 0 rgba(211, 47, 47, 0); }
        }
        
        .btn:hover {
            background: var(--primary-dark);
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(211, 47, 47, 0.6);
            animation: none;
        }
        
        .btn-secondary {
            background: transparent;
            border: 2px solid var(--secondary);
            color: var(--secondary);
            animation: pulse-btn-secondary 2s infinite;
        }
        
        @keyframes pulse-btn-secondary {
            0% { box-shadow: 0 0 0 0 rgba(255, 193, 7, 0.7); }
            70% { box-shadow: 0 0 0 15px rgba(255, 193, 7, 0); }
            100% { box-shadow: 0 0 0 0 rgba(255, 193, 7, 0); }
        }
        
        .btn-secondary:hover {
            background: var(--secondary);
            color: var(--dark);
            animation: none;
        }
        
        /* العدادات التصاعدية */
        .counters {
            padding: 60px 0;
            background: rgba(0, 0, 0, 0.7);
        }
        
        .counters-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
        }
        
        .counter-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            border: 1px solid rgba(211, 47, 47, 0.3);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }
        
        .counter-icon {
            font-size: 40px;
            color: var(--secondary);
            margin-bottom: 15px;
        }
        
        .counter-number {
            font-size: 42px;
            font-weight: bold;
            color: var(--light);
            margin-bottom: 10px;
        }
        
        .counter-text {
            color: #ccc;
            font-size: 18px;
        }
        
        /* ميزات */
        .features {
            padding: 60px 0;
            background: rgba(0, 0, 0, 0.7);
        }
        
        .section-title {
            text-align: center;
            font-size: 36px;
            margin-bottom: 40px;
            color: var(--light);
            position: relative;
            padding-bottom: 15px;
        }
        
        .section-title:after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 100px;
            height: 3px;
            background: var(--primary);
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }
        
        .feature-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            transition: all 0.3s ease;
            border: 1px solid rgba(211, 47, 47, 0.3);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }
        
        .feature-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4);
            border-color: var(--primary);
        }
        
        .feature-icon {
            font-size: 50px;
            color: var(--secondary);
            margin-bottom: 20px;
        }
        
        .feature-card h3 {
            font-size: 24px;
            margin-bottom: 15px;
            color: var(--light);
        }
        
        .feature-card p {
            color: #ccc;
        }
        
        /* قسم العملاء */
        .testimonials {
            padding: 60px 0;
            background: rgba(0, 0, 0, 0.5);
        }
        
        .testimonial-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }
        
        .testimonial-card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 25px;
            border: 1px solid rgba(255, 193, 7, 0.3);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }
        
        .testimonial-text {
            font-style: italic;
            margin-bottom: 20px;
            color: #eee;
        }
        
        .testimonial-author {
            display: flex;
            align-items: center;
        }
        
        .testimonial-avatar {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: var(--secondary);
            display: flex;
            align-items: center;
            justify-content: center;
            margin-left: 15px;
            font-weight: bold;
            font-size: 20px;
        }
        
        .testimonial-info h4 {
            color: var(--light);
            margin-bottom: 5px;
        }
        
        .testimonial-info p {
            color: var(--secondary);
            font-size: 14px;
        }
        
        /* قسم الأسئلة الشائعة */
        .faq {
            padding: 60px 0;
            background: rgba(0, 0, 0, 0.7);
        }
        
        .faq-item {
            margin-bottom: 20px;
            border-radius: 10px;
            overflow: hidden;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(211, 47, 47, 0.3);
        }
        
        .faq-question {
            padding: 20px;
            background: rgba(211, 47, 47, 0.2);
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-weight: bold;
            font-size: 18px;
        }
        
        .faq-answer {
            padding: 0 20px;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease;
        }
        
        .faq-answer.active {
            padding: 20px;
            max-height: 500px;
        }
        
        /* روبوت الدردشة */
        .chatbot {
            position: fixed;
            bottom: 30px;
            left: 30px;
            z-index: 1000;
        }
        
        .chatbot-btn {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: var(--primary);
            color: var(--light);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
            animation: pulse-chat 2s infinite;
        }
        
        @keyframes pulse-chat {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        
        .chatbot-btn:hover {
            transform: scale(1.1);
            animation: none;
        }
        
        .chatbot-window {
            position: fixed;
            bottom: 100px;
            left: 30px;
            width: 350px;
            height: 450px;
            background: var(--dark);
            border-radius: 15px;
            box-shadow: 0 5px 25px rgba(0, 0, 0, 0.5);
            display: none;
            flex-direction: column;
            overflow: hidden;
            border: 2px solid var(--primary);
        }
        
        .chatbot-header {
            background: var(--primary);
            padding: 15px;
            color: var(--light);
            font-weight: bold;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .chatbot-close {
            cursor: pointer;
            font-size: 20px;
        }
        
        .chatbot-messages {
            flex: 1;
            padding: 15px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
        }
        
        .message {
            max-width: 80%;
            padding: 10px 15px;
            margin-bottom: 10px;
            border-radius: 15px;
            font-size: 14px;
        }
        
        .bot-message {
            background: rgba(211, 47, 47, 0.2);
            align-self: flex-start;
            border-bottom-right-radius: 0;
        }
        
        .user-message {
            background: rgba(255, 193, 7, 0.2);
            align-self: flex-end;
            border-bottom-left-radius: 0;
        }
        
        .chatbot-input {
            display: flex;
            padding: 10px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .chatbot-input input {
            flex: 1;
            padding: 10px;
            border: none;
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.1);
            color: var(--light);
            margin-right: 10px;
        }
        
        .chatbot-input button {
            background: var(--primary);
            color: var(--light);
            border: none;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            cursor: pointer;
        }
        
        /* جدول القروض */
        .loan-table {
            width: 100%;
            border-collapse: collapse;
            margin: 30px 0;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            overflow: hidden;
        }
        
        .loan-table th, .loan-table td {
            padding: 15px;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .loan-table th {
            background: var(--primary);
            color: var(--light);
        }
        
        .loan-table tr:nth-child(even) {
            background: rgba(255, 255, 255, 0.02);
        }
        
        .loan-table-container {
            overflow-x: auto;
        }
        
        /* الفوتر */
        footer {
            background: rgba(0, 0, 0, 0.9);
            padding: 40px 0 20px;
            border-top: 2px solid var(--primary);
        }
        
        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            margin-bottom: 30px;
        }
        
        .footer-section h3 {
            color: var(--secondary);
            margin-bottom: 20px;
            font-size: 20px;
        }
        
        .footer-section p, .footer-section a {
            color: #ccc;
            margin-bottom: 10px;
            display: block;
            text-decoration: none;
            transition: color 0.3s ease;
        }
        
        .footer-section a:hover {
            color: var(--secondary);
        }
        
        .footer-bottom {
            text-align: center;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: #999;
            font-size: 14px;
        }
        
        /* قسم الشروط والخصوصية */
        .terms {
            padding: 60px 0;
            background: rgba(0, 0, 0, 0.5);
        }
        
        .terms-content {
            background: rgba(255, 255, 255, 0.05);
            padding: 30px;
            border-radius: 15px;
            border: 1px solid rgba(211, 47, 47, 0.3);
        }
        
        .terms-section {
            margin-bottom: 30px;
        }
        
        .terms-section h3 {
            color: var(--secondary);
            margin-bottom: 15px;
            font-size: 22px;
        }
        
        .terms-section p, .terms-section ul {
            color: #ccc;
            margin-bottom: 15px;
        }
        
        .terms-section ul {
            padding-right: 20px;
        }
        
        .terms-section li {
            margin-bottom: 10px;
        }
        
        /* قسم التسجيل */
        .register {
            padding: 60px 0;
            text-align: center;
            background: rgba(0, 0, 0, 0.7);
        }
        
        .register-box {
            background: rgba(255, 255, 255, 0.05);
            padding: 40px;
            border-radius: 15px;
            border: 2px solid var(--secondary);
            max-width: 600px;
            margin: 0 auto;
        }
        
        .register-box h2 {
            color: var(--secondary);
            margin-bottom: 20px;
        }
        
        .register-box p {
            margin-bottom: 30px;
            color: #ccc;
        }
        
        /* التكيف مع الشاشات الصغيرة */
        @media (max-width: 768px) {
            .header-content {
                flex-direction: column;
                text-align: center;
            }
            
            .logo {
                margin-bottom: 15px;
            }
            
            .hero h1 {
                font-size: 32px;
            }
            
            .hero p {
                font-size: 18px;
            }
            
            .btn {
                padding: 12px 25px;
                font-size: 16px;
            }
            
            .section-title {
                font-size: 28px;
            }
            
            .chatbot {
                left: 15px;
                bottom: 15px;
            }
            
            .chatbot-window {
                width: 300px;
                height: 400px;
                left: 15px;
            }
            
            .loan-table th, .loan-table td {
                padding: 10px;
                font-size: 12px;
            }
            
            .counter-number {
                font-size: 32px;
            }
        }
    </style>
</head>
<body>
    <!-- الشريط المتحرك العلوي -->
    <div class="top-ticker">
        <div class="ticker-content">
            <span class="ticker-item">🎉 مبروك أحمد محمد - تمت الموافقة على 45,000 جنيه</span>
            <span class="ticker-item">✅ مبروك فاطمة علي - تمت الموافقة على 75,000 جنيه</span>
            <span class="ticker-item">🎊 مبروك محمود حسن - تمت الموافقة على 60,000 جنيه</span>
            <span class="ticker-item">⭐ مبروك سارة محمد - تمت الموافقة على 85,000 جنيه</span>
            <span class="ticker-item">🎯 مبروك خالد أحمد - تمت الموافقة على 120,000 جنيه</span>
        </div>
    </div>

    <!-- الهيدر -->
    <header>
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <div class="logo-text">Cash Faster</div>
                    <div class="logo-icon">⚡</div>
                </div>
                <div>
                    <a href="#apply" class="btn">قدم طلبك الآن</a>
                </div>
            </div>
        </div>
    </header>

    <!-- قسم البطل -->
    <section class="hero">
        <div class="container">
            <h1>أفضل وأسرع <span class="highlight">قرض في مصر</span></h1>
            <p>احصل على قرضك النقدي بسرعة وسهولة، <span class="highlight">بدون دفع مليم واحد مقدماً</span>، وبأقل فائدة في السوق</p>
            <div>
                <a href="#apply" class="btn">قدم طلبك الآن</a>
                <a href="#conditions" class="btn btn-secondary">شروط القرض</a>
            </div>
        </div>
    </section>

    <!-- العدادات التصاعدية -->
    <section class="counters">
        <div class="container">
            <h2 class="section-title">إحصائيات كاش فاستر</h2>
            <div class="counters-grid">
                <div class="counter-card">
                    <div class="counter-icon">👥</div>
                    <div class="counter-number" id="counter1">0</div>
                    <div class="counter-text">عملاء مسجلين</div>
                </div>
                <div class="counter-card">
                    <div class="counter-icon">✅</div>
                    <div class="counter-number" id="counter2">0</div>
                    <div class="counter-text">عميل تمت الموافقة عليهم</div>
                </div>
                <div class="counter-card">
                    <div class="counter-icon">💰</div>
                    <div class="counter-number" id="counter3">0</div>
                    <div class="counter-text">عميل تم صرف القرض لهم</div>
                </div>
                <div class="counter-card">
                    <div class="counter-icon">⏳</div>
                    <div class="counter-number" id="counter4">0</div>
                    <div class="counter-text">عميل في قائمة الانتظار</div>
                </div>
            </div>
        </div>
    </section>

    <!-- الميزات -->
    <section class="features">
        <div class="container">
            <h2 class="section-title">لماذا تختار كاش فاستر؟</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <h3>أسرع قرض في مصر</h3>
                    <p>احصل على موافقة مبدئية خلال دقائق وتمويل كامل خلال 48 ساعة</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">💰</div>
                    <h3>بدون أي مصاريف مقدمة</h3>
                    <p>لا توجد أي رسوم أو مصاريف خفية، تدفع فقط أقساط القرض</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📱</div>
                    <h3>استلام القرض فوري</h3>
                    <p>استلم قرضك مباشرة على محفظتك الإلكترونية (فودافون كاش/اتصالات كاش)</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🛡️</div>
                    <h3>آمن ومضمون</h3>
                    <p>بياناتك محمية بنظام أمان متكامل وخصوصية تامة</p>
                </div>
            </div>
        </div>
    </section>

    <!-- شروط القرض -->
    <section class="terms" id="conditions">
        <div class="container">
            <h2 class="section-title">شروط الحصول على القرض</h2>
            <div class="terms-content">
                <div class="terms-section">
                    <h3>📝 الشروط الأساسية</h3>
                    <ul>
                        <li>السن: يجب أن يكون العميل بين 21 و 65 سنة</li>
                        <li>المستندات: صورة من البطاقة الشخصية (أمامي/خلفي) وصورة سيلفي مع البطاقة</li>
                        <li>محفظة إلكترونية: يجب أن تكون محفظتك كاش مسجلة باسمك (فودافون كاش/اتصالات كاش)</li>
                        <li>الضامن: يجب وجود ضامن من الدرجة الأولى (أخ، أم، زوج، إلخ)</li>
                    </ul>
                </div>
                
                <div class="terms-section">
                    <h3>💰 تفاصيل القروض والأقساط</h3>
                    <div class="loan-table-container">
                        <table class="loan-table">
                            <thead>
                                <tr>
                                    <th>مبلغ القرض</th>
                                    <th>المدة (شهر)</th>
                                    <th>القسط الشهري</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr><td>30,000 جنيه</td><td>12</td><td>3,325 جنيه</td></tr>
                                <tr><td>35,000 جنيه</td><td>12</td><td>3,875 جنيه</td></tr>
                                <tr><td>40,000 جنيه</td><td>18</td><td>2,965 جنيه</td></tr>
                                <tr><td>45,000 جنيه</td><td>18</td><td>3,325 جنيه</td></tr>
                                <tr><td>50,000 جنيه</td><td>24</td><td>2,725 جنيه</td></tr>
                                <tr><td>55,000 جنيه</td><td>24</td><td>3,075 جنيه</td></tr>
                                <tr><td>60,000 جنيه</td><td>24</td><td>3,085 جنيه</td></tr>
                                <tr><td>65,000 جنيه</td><td>26</td><td>3,325 جنيه</td></tr>
                                <tr><td>70,000 جنيه</td><td>26</td><td>3,585 جنيه</td></tr>
                                <tr><td>75,000 جنيه</td><td>26</td><td>3,845 جنيه</td></tr>
                                <tr><td>80,000 جنيه</td><td>30</td><td>3,550 جنيه</td></tr>
                                <tr><td>85,000 جنيه</td><td>30</td><td>3,775 جنيه</td></tr>
                                <tr><td>90,000 جنيه</td><td>30</td><td>3,990 جنيه</td></tr>
                                <tr><td>95,000 جنيه</td><td>30</td><td>4,220 جنيه</td></tr>
                                <tr><td>100,000 جنيه</td><td>32</td><td>4,157 جنيه</td></tr>
                                <tr><td>105,000 جنيه</td><td>32</td><td>4,375 جنيه</td></tr>
                                <tr><td>110,000 جنيه</td><td>32</td><td>4,580 جنيه</td></tr>
                                <tr><td>115,000 جنيه</td><td>38</td><td>4,075 جنيه</td></tr>
                                <tr><td>120,000 جنيه</td><td>38</td><td>4,235 جنيه</td></tr>
                                <tr><td>125,000 جنيه</td><td>38</td><td>4,035 جنيه</td></tr>
                                <tr><td>130,000 جنيه</td><td>42</td><td>4,400 جنيه</td></tr>
                                <tr><td>135,000 جنيه</td><td>42</td><td>4,305 جنيه</td></tr>
                                <tr><td>140,000 جنيه</td><td>42</td><td>4,495 جنيه</td></tr>
                                <tr><td>145,000 جنيه</td><td>48</td><td>4,075 جنيه</td></tr>
                                <tr><td>150,000 جنيه</td><td>48</td><td>4,205 جنيه</td></tr>
                                <tr><td>155,000 جنيه</td><td>48</td><td>4,315 جنيه</td></tr>
                                <tr><td>160,000 جنيه</td><td>48</td><td>4,435 جنيه</td></tr>
                                <tr><td>165,000 جنيه</td><td>48</td><td>4,615 جنيه</td></tr>
                                <tr><td>170,000 جنيه</td><td>48</td><td>4,725 جنيه</td></tr>
                                <tr><td>175,000 جنيه</td><td>48</td><td>4,848 جنيه</td></tr>
                                <tr><td>180,000 جنيه</td><td>54</td><td>4,435 جنيه</td></tr>
                                <tr><td>185,000 جنيه</td><td>54</td><td>4,557 جنيه</td></tr>
                                <tr><td>190,000 جنيه</td><td>60</td><td>4,215 جنيه</td></tr>
                                <tr><td>195,000 جنيه</td><td>60</td><td>4,325 جنيه</td></tr>
                                <tr><td>200,000 جنيه</td><td>60</td><td>4,440 جنيه</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- طريقة السداد -->
    <section class="features">
        <div class="container">
            <h2 class="section-title">💰 طريقة سداد الأقساط</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">📋</div>
                    <h3>كود مرجعي شهري</h3>
                    <p>بيتم إرسال كود مرجعي خاص بيك كل شهر قبل موعد الدفع</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🧾</div>
                    <h3>الدفع عبر فوري باي</h3>
                    <p>القسط بيتدفع من خلال "فوري باي" – كود الخدمة: 788</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📞</div>
                    <h3>نفس رقم التسجيل</h3>
                    <p>لازم الدفع يتم بنفس الرقم اللي سجلت به، علشان القسط يتسجل باسمك</p>
                </div>
            </div>
        </div>
    </section>

    <!-- قسم التسجيل -->
    <section class="register" id="apply">
        <div class="container">
            <h2 class="section-title">قدم طلبك الآن</h2>
            <div class="register-box">
                <h2>سجل طلبك الآن واحصل على قرضك</h2>
                <p>املأ الاستمارة الإلكترونية وسيقوم فريقنا بمراجعة طلبك والتواصل معك في أقرب وقت</p>
                <a href="https://cashfast-tbmf22.manus.space" class="btn">سجل طلبك الآن</a>
            </div>
        </div>
    </section>

    <!-- قسم الأسئلة الشائعة -->
    <section class="faq">
        <div class="container">
            <h2 class="section-title">الأسئلة الشائعة</h2>
            
            <div class="faq-item">
                <div class="faq-question" onclick="toggleFaq(0)">
                    ما هي شروط التقديم على القرض؟
                    <span class="faq-icon">+</span>
                </div>
                <div class="faq-answer">
                    <p>السن: يجب أن يكون العميل بين 21 و 65 سنة.<br>
                    المستندات: صورة من البطاقة الشخصية (أمامي/خلفي) وصورة سيلفي مع البطاقة.<br>
                    محفظة إلكترونية: يجب أن تكون محفظتك كاش مسجلة باسمك.<br>
                    الضامن: يجب وجود ضامن من الدرجة الأولى (أخ، أم، زوج، إلخ).</p>
                </div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question" onclick="toggleFaq(1)">
                    كيف يمكنني التقديم على القرض؟
                    <span class="faq-icon">+</span>
                </div>
                <div class="faq-answer">
                    <p>لتقديم طلبك، يرجى تعبئة النموذج هذا: <a href="https://cashfast-tbmf22.manus.space" style="color: #FFC107;">https://cashfast-tbmf22.manus.space</a>. بمجرد استلامنا لبياناتك، سنقوم بمراجعتها والتواصل معك.</p>
                </div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question" onclick="toggleFaq(2)">
                    هل يمكنني الحصول على القرض بدون دفع أموال وبدون وظيفة؟
                    <span class="faq-icon">+</span>
                </div>
                <div class="faq-answer">
                    <p>نعم! لا نحتاج إلى وظيفة ولا يوجد دفع أو تحويل أي رسوم أو مصاريف نهائيا تحت أي مسمى. نحن نقدم قروض بدون متطلبات وظيفية.</p>
                </div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question" onclick="toggleFaq(3)">
                    هل ليكم علاقة بالايسكور؟
                    <span class="faq-icon">+</span>
                </div>
                <div class="faq-answer">
                    <p>لا يوجد لدينا علاقة بالايسكور نهائياً. معاملاتنا مستقلة تماماً ولا تؤثر على تقييمك الائتماني في أي جهة أخرى.</p>
                </div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question" onclick="toggleFaq(4)">
                    هل متاح لجميع المحافظات؟
                    <span class="faq-icon">+</span>
                </div>
                <div class="faq-answer">
                    <p>نعم! لدينا شركة مندوبين في جميع أنحاء الجمهورية لتغطية أكبر عدد من العملاء. نحن نخدم جميع محافظات مصر.</p>
                </div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question" onclick="toggleFaq(5)">
                    كم من الوقت يستغرق الموافقة على القرض؟
                    <span class="faq-icon">+</span>
                </div>
                <div class="faq-answer">
                    <p>في العادة، يتم الموافقة على القرض خلال 48 ساعة بحد أقصى من تقديم الطلب، ويعتمد ذلك على سرعة استكمال المستندات المطلوبة.</p>
                </div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question" onclick="toggleFaq(6)">
                    هل هناك رسوم إضافية بعد الموافقة؟
                    <span class="faq-icon">+</span>
                </div>
                <div class="faq-answer">
                    <p>لا توجد أي رسوم إضافية أو مصاريف أخرى بعد الموافقة على القرض. الفائدة فقط مدمجة في القسط الشهري.</p>
                </div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question" onclick="toggleFaq(7)">
                    هل يمكنني سداد القرض قبل موعد الاستحقاق؟
                    <span class="faq-icon">+</span>
                </div>
                <div class="faq-answer">
                    <p>نعم، يمكنك سداد القرض في أي وقت قبل الموعد المحدد. وفي هذه الحالة، سيتم احتساب الفائدة حتى تاريخ السداد.</p>
                </div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question" onclick="toggleFaq(8)">
                    ماذا يحدث إذا لم أتمكن من سداد القرض في الوقت المحدد؟
                    <span class="faq-icon">+</span>
                </div>
                <div class="faq-answer">
                    <p>إذا تأخرت في السداد، قد تترتب عليك رسوم تأخير وفقًا للاتفاق المبرم.</p>
                </div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question" onclick="toggleFaq(9)">
                    هل يمكنني تعديل قيمة القرض أو مدة السداد بعد الموافقة؟
                    <span class="faq-icon">+</span>
                </div>
                <div class="faq-answer">
                    <p>لا يمكن تعديل القرض بعد الموافقة عليه. إذا كنت بحاجة لتغيير المبلغ أو المدة، يمكنك طلب قرض جديد.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- قسم الخصوصية -->
    <section class="terms">
        <div class="container">
            <h2 class="section-title">سياسة الخصوصية والبيانات</h2>
            <div class="terms-content">
                <div class="terms-section">
                    <h3>🔒 جمع المعلومات</h3>
                    <p>نقوم بجمع المعلومات التالية فقط:</p>
                    <ul>
                        <li>المعلومات الشخصية: الاسم، رقم الهاتف، رقم محفظتك فودافون كاش، والعنوان.</li>
                        <li>المعلومات المالية: قيمة القرض المطلوب، مدة السداد، وبيانات الدخل.</li>
                        <li>المستندات: صورة البطاقة الشخصية، صورة سيلفي، إيصال مرافق حديث، وأي مستندات مطلوبة أخرى.</li>
                    </ul>
                </div>
                
                <div class="terms-section">
                    <h3>📊 كيفية استخدام المعلومات</h3>
                    <p>نستخدم المعلومات التي تقدمها للغرض الوحيد وهو:</p>
                    <ul>
                        <li>مراجعة طلبات القروض.</li>
                        <li>التواصل معك لإتمام الإجراءات اللازمة.</li>
                        <li>تحليل البيانات لتحسين الخدمة وتقديم أفضل العروض المالية.</li>
                    </ul>
                </div>
                
                <div class="terms-section">
                    <h3>🛡️ حماية البيانات</h3>
                    <p>نحن نلتزم بتطبيق إجراءات أمنية صارمة لحماية بياناتك الشخصية. يتم تشفير جميع المعلومات المرسلة عبر الإنترنت باستخدام أحدث تقنيات التشفير.</p>
                </div>
                
                <div class="terms-section">
                    <h3>🤝 مشاركة المعلومات</h3>
                    <p>نحن نلتزم بالحفاظ على سرية بياناتك الشخصية. لن نقوم بمشاركة أو بيع بياناتك الشخصية لأطراف ثالثة إلا إذا كان ذلك مطلوبًا بموجب القانون.</p>
                </div>
                
                <div class="terms-section">
                    <h3>⏳ الاحتفاظ بالبيانات</h3>
                    <p>سنحتفظ بمعلوماتك فقط طالما كانت هناك حاجة لذلك لتلبية الأغراض التي تم جمعها من أجلها.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- الفوتر -->
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>عن كاش فاستر</h3>
                    <p>نقدّم لك طريقة ذكية وسريعة للحصول على قرض نقدي فوري، من دون الحاجة لشراء أي سلعة أو دفع أي مبلغ مقدم.</p>
                </div>
                
                <div class="footer-section">
                    <h3>روابط سريعة</h3>
                    <a href="#conditions">شروط القرض</a>
                    <a href="#apply">تقديم طلب</a>
                    <a href="#">طريقة السداد</a>
                    <a href="#">الأسئلة الشائعة</a>
                </div>
                
                <div class="footer-section">
                    <h3>معلومات التواصل</h3>
                    <p>فريق الدعم موجود يوميًا من الساعة 7 صباحًا حتى 10 مساءً</p>
                    <p>للاستفسارات: ابعتلنا رسالة هنا على الصفحة</p>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>© 2023 Cash Faster. جميع الحقوق محفوظة</p>
            </div>
        </div>
    </footer>

    <!-- روبوت الدردشة -->
    <div class="chatbot">
        <div class="chatbot-btn" onclick="toggleChatbot()">
            <i class="fas fa-robot"></i>
        </div>
        <div class="chatbot-window" id="chatbotWindow">
            <div class="chatbot-header">
                <span>مساعد كاش فاستر</span>
                <span class="chatbot-close" onclick="toggleChatbot()">×</span>
            </div>
            <div class="chatbot-messages" id="chatbotMessages">
                <div class="message bot-message">
                    أهلاً وسهلاً بك! أنا مساعد كاش فاستر، كيف يمكنني مساعدتك اليوم؟
                </div>
            </div>
            <div class="chatbot-input">
                <input type="text" id="userInput" placeholder="اكتب رسالتك هنا...">
                <button onclick="sendMessage()"><i class="fas fa-paper-plane"></i></button>
            </div>
        </div>
    </div>

    <script>
        // تباعد الأسئلة الشائعة
        function toggleFaq(index) {
            const answers = document.querySelectorAll('.faq-answer');
            const icons = document.querySelectorAll('.faq-icon');
            
            if (answers[index].classList.contains('active')) {
                answers[index].classList.remove('active');
                icons[index].textContent = '+';
            } else {
                answers[index].classList.add('active');
                icons[index].textContent = '-';
            }
        }
        
        // روبوت الدردشة
        function toggleChatbot() {
            const chatbotWindow = document.getElementById('chatbotWindow');
            if (chatbotWindow.style.display === 'flex') {
                chatbotWindow.style.display = 'none';
            } else {
                chatbotWindow.style.display = 'flex';
            }
        }
        
        function sendMessage() {
            const userInput = document.getElementById('userInput');
            const message = userInput.value.trim();
            
            if (message === '') return;
            
            // إضافة رسالة المستخدم
            const userMessage = document.createElement('div');
            userMessage.classList.add('message', 'user-message');
            userMessage.textContent = message;
            document.getElementById('chatbotMessages').appendChild(userMessage);
            
            // مسح حقل الإدخال
            userInput.value = '';
            
            // التمرير لأسفل
            const messagesContainer = document.getElementById('chatbotMessages');
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
            
            // معالجة الرسالة وإضافة الرد
            setTimeout(() => {
                let response = '';
                
                if (message.includes('شروط') || message.includes('مطلوب') || message.includes('مستندات')) {
                    response = 'شروط التقديم على القرض:\n- السن: بين 21 و 65 سنة\n- المستندات: صورة البطاقة الشخصية (أمامي/خلفي) وصورة سيلفي مع البطاقة\n- محفظة إلكترونية: يجب أن تكون محفظتك كاش مسجلة باسمك\n- الضامن: يجب وجود ضامن من الدرجة الأولى (أخ، أم، زوج، إلخ)';
                } else if (message.includes('قدم') || message.includes('طلب') || message.includes('تسجيل') || message.includes('رابط')) {
                    response = 'لتقديم طلبك، يرجى تعبئة النموذج الإلكتروني من خلال الرابط: https://cashfast-tbmf22.manus.space\n\nسيقوم فريقنا بمراجعة طلبك والتواصل معك في أقرب وقت!';
                } else if (message.includes('وظيفة') || message.includes('بدون وظيفة') || message.includes('رسوم') || message.includes('مصاريف')) {
                    response = 'نعم! لا نحتاج إلى وظيفة ولا يوجد دفع أو تحويل أي رسوم أو مصاريف نهائيا تحت أي مسمى. نحن نقدم قروض بدون متطلبات وظيفية وبدون أي مصاريف خفية.';
                } else if (message.includes('ايسكور') || message.includes('تقييم') || message.includes('ائتمان')) {
                    response = 'لا يوجد لدينا علاقة بالايسكور نهائياً. معاملاتنا مستقلة تماماً ولا تؤثر على تقييمك الائتماني في أي جهة أخرى.';
                } else if (message.includes('محافظة') || message.includes('محافظات') || message.includes('مناطق')) {
                    response = 'نعم! لدينا شركة مندوبين في جميع أنحاء الجمهورية لتغطية أكبر عدد من العملاء. نحن نخدم جميع محافظات مصر بدون استثناء.';
                } else if (message.includes('وقت') || message.includes('مدة') || message.includes('موافقة')) {
                    response = 'في العادة، يتم الموافقة على القرض خلال 48 ساعة بحد أقصى من تقديم الطلب، ويعتمد ذلك على سرعة استكمال المستندات المطلوبة.';
                } else if (message.includes('سداد') || message.includes('قسط') || message.includes('دفع')) {
                    response = 'طريقة سداد الأقساط:\n- بيتم إرسال كود مرجعي خاص بيك كل شهر قبل موعد الدفع\n- القسط بيتدفع من خلال "فوري باي" – كود الخدمة: 788\n- لازم الدفع يتم بنفس الرقم اللي سجلت به، علشان القسط يتسجل باسمك';
                } else if (message.includes('تعديل') || message.includes('تغيير') || message.includes('مبلغ')) {
                    response = 'لا يمكن تعديل القرض بعد الموافقة عليه. إذا كنت بحاجة لتغيير المبلغ أو المدة، يمكنك طلب قرض جديد.';
                } else if (message.includes('تأخر') || message.includes('متأخر') || message.includes('تأخير')) {
                    response = 'إذا تأخرت في السداد، قد تترتب عليك رسوم تأخير وفقًا للاتفاق المبرم.';
                } else if (message.includes('خصوصية') || message.includes('بيانات') || message.includes('أمان')) {
                    response = 'بياناتك محمية بنظام أمان متكامل. نحن نلتزم بالحفاظ على سرية بياناتك الشخصية ولن نقوم بمشاركة أو بيع بياناتك لأطراف ثالثة إلا إذا كان ذلك مطلوبًا بموجب القانون.';
                } else {
                    response = 'شكراً لاستفسارك! كيف يمكنني مساعدتك بشكل أكثر تحديداً؟ يمكنني الإجابة على استفساراتك حول شروط القرض، مدة الموافقة، طريقة السداد، وغيرها من الأمور المتعلقة بخدماتنا.';
                }
                
                // إضافة رد المساعد
                const botMessage = document.createElement('div');
                botMessage.classList.add('message', 'bot-message');
                botMessage.textContent = response;
                document.getElementById('chatbotMessages').appendChild(botMessage);
                
                // التمرير لأسفل
                messagesContainer.scrollTop = messagesContainer.scrollHeight;
            }, 1000);
        }
        
        // السماح بإرسال الرسالة بالضغط على Enter
        document.getElementById('userInput').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
        
        // العدادات التصاعدية
        function animateCounter(element, finalValue, duration) {
            let startTime = null;
            const startValue = 0;
            const step = (timestamp) => {
                if (!startTime) startTime = timestamp;
                const progress = Math.min((timestamp - startTime) / duration, 1);
                const currentValue = Math.floor(progress * (finalValue - startValue) + startValue);
                element.textContent = currentValue.toLocaleString();
                if (progress < 1) {
                    window.requestAnimationFrame(step);
                } else {
                    element.textContent = finalValue.toLocaleString();
                }
            };
            window.requestAnimationFrame(step);
        }
        
        // تشغيل العدادات عند التمرير إليها
        function initCounters() {
            const counter1 = document.getElementById('counter1');
            const counter2 = document.getElementById('counter2');
            const counter3 = document.getElementById('counter3');
            const counter4 = document.getElementById('counter4');
            
            // قيم العدادات (يمكن تعديلها)
            animateCounter(counter1, 4850, 2000);
            animateCounter(counter2, 3820, 2000);
            animateCounter(counter3, 2950, 2000);
            animateCounter(counter4, 920, 2000);
        }
        
        // بدء العدادات عندما يصبح القسم مرئياً
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    initCounters();
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });
        
        observer.observe(document.querySelector('.counters'));
    </script>
</body>
</html>