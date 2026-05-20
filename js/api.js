function fetchReadings(word) {
    var baseUrl = CONFIG.API_BASE_URL;
    var endpoint = CONFIG.ENDPOINTS.READINGS;
    var params = '?word=' + encodeURIComponent(word.trim());
    var url = baseUrl + endpoint + params;
    return fetch(url)
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Ошибка сервера: ' + response.status);
            }
            return response.json();
        });
}
