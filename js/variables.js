var CONFIG = {
    API_BASE_URL: (
        window.location.hostname === 'localhost' ||
        window.location.hostname === '127.0.0.1' ||
        window.location.hostname === ''
    )
        ? 'http://localhost:8080'
        : 'https://bbamf0mf8kfcd675bt1e.containers.yandexcloud.net',

    ENDPOINTS: {
        READINGS: '/readings'
    }
};
