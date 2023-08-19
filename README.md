<h1>Телефонная Авторизация API</h1>

<p>Добро пожаловать в документацию Телефонной Авторизации API. Этот API предоставляет возможность авторизации пользователей по номеру телефона, создания профилей и использования инвайт-кодов.</p>

<h2>Установка и настройка</h2>

<ol>
  <li>Клонируйте репозиторий:
    <pre><code>git clone https://github.com/yPavelAndrushkevich/phone-auth.git
    cd phone-auth</code></pre>
  </li>
  <li>Установите зависимости:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Примените миграции:
    <pre><code>python manage.py migrate</code></pre>
  </li>
</ol>

<h2>Использование API</h2>

<h3>Авторизация</h3>

<p><strong>Запрос на ввод номера телефона и кода авторизации:</strong></p>

<ul>
  <li>Метод: <code>POST</code></li>
  <li>URL: <code>/api/login/</code></li>
</ul>

<p><strong>Пример запроса:</strong></p>
<pre><code>{
  "phone_number": "1234567890"
}</code></pre>

<p><strong>Ввод кода авторизации:</strong></p>

<ul>
  <li>Метод: <code>POST</code></li>
  <li>URL: <code>/api/verify/</code></li>
</ul>

<p><strong>Пример запроса:</strong></p>
<pre><code>{
  "phone_number": "1234567890",
  "verification_code": "1234"
}</code></pre>

<h3>Профиль пользователя</h3>

<p><strong>Получение профиля пользователя:</strong></p>

<ul>
  <li>Метод: <code>GET</code></li>
  <li>URL: <code>/api/profile/</code></li>
</ul>

<h3>Список пользователей, использующих инвайт-код текущего пользователя</h3>

<p><strong>Получение списка пользователей:</strong></p>

<ul>
  <li>Метод: <code>GET</code></li>
  <li>URL: <code>/api/invited-users/</code></li>
</ul>

<p><strong>Пример успешного ответа:</strong></p>
<pre><code>[
  {
    "phone_number": "9876543210"
  },
  {
    "phone_number": "5555555555"
  }
]</code></pre>

<h3>Аутентификация</h3>

<p>Для доступа к защищенным эндпоинтам API используйте токены. Добавьте токен в заголовок запроса:</p>

<pre><code>Authorization: Token your_generated_token_here</code></pre>

<h2>Заметки</h2>

<ul>
  <li>Этот API предоставляется в качестве демонстрационного примера и не предназначен для использования в продакшене.</li>
  <li>Обязательно настройте параметры базы данных, безопасности и другие настройки перед развертыванием в реальной среде.</li>
  <li>Поддержка:p.andrushkevich@gmail.com</li>
</ul>


