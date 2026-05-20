function runSimulation() {
    var wordInput = document.getElementById('wordInput');
    var word = wordInput.value;
    if (!word || !word.trim()) {
        showStatus('Ошибка: Поле ввода пустое!');
        return;
    }
    showStatus('Запрос к бэкенду...');
    clearResults();
    fetchReadings(word)
        .then(function(data) {
            showStatus('OK.');
            renderResults(data);
        })
        .catch(function(error) {
            showStatus('Ошибка соединения.');
            document.getElementById('resultsLayer').innerHTML =
                '<p style="color: red; font-weight: bold;">' +
                'Не удалось получить данные.<br/>' +
                '<span style="font-size: 12px; font-family: monospace; font-weight: normal;">Детали: ' + error.message + '</span>' +
                '</p>';
        });
}
