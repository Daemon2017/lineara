function renderResults(data) {
    var resultsContainer = document.getElementById('resultsLayer');
    if (!data || data.length === 0) {
        resultsContainer.innerHTML = '<p>Бэкенд вернул пустой список вариантов.</p>';
        return;
    }
    var html = '';
    for (var i = 0; i < data.length; i++) {
        var v = data[i];
        html += '<div style="margin-bottom: 20px; padding: 15px; border: 1px solid #ccc; background-color: #f9f9f9; border-radius: 4px;">';
        html += '  <h3 style="margin-top: 0; color: #d97706;">Ударный слог #' + v.stressed_syllable_number + '</h3>';
        html += '  <p>Пре-ПИЕ: <code style="background: #f3e8ff; color: #6b21a8; padding: 2px 6px; font-weight: bold;">' + v.pre_pie_r + '</code></p>';
        html += '</div>';
    }
    resultsContainer.innerHTML = html;
}

function showStatus(text) {
    document.getElementById('stateLabel').textContent = text;
}

function clearResults() {
    document.getElementById('resultsLayer').innerHTML = '';
}
