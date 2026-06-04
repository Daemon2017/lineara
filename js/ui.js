function renderResults(data) {
    var resultsContainer = document.getElementById('resultsLayer');
    if (!data || data.length === 0) {
        resultsContainer.innerHTML = '<p>Бэкенд вернул пустой список вариантов.</p>';
        return;
    }
    var html = '';
    for (var i = 0; i < data.length; i++) {
        var v = data[i];
        html += '<div style="margin-bottom: 25px; padding: 20px; border: 1px solid #e2e8f0; background-color: #ffffff; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">';
        html += '  <h3 style="margin-top: 0; margin-bottom: 10px; color: #d97706; font-size: 1.2rem;">Ударный слог #' + v.stressed_syllable_number + '</h3>';
        html += '  <div style="margin-bottom: 15px;"><span style="font-size: 12px; color: #718096; display: block; margin-bottom: 4px;">Минойская форма:</span><code style="background: #f3e8ff; color: #6b21a8; padding: 4px 8px; font-weight: bold; border-radius: 4px; font-size: 14px;">' + v.minoan + '</code></div>';
        html += '  <span style="font-size: 12px; color: #718096; display: block; margin-bottom: 6px;">Найденные когнаты:</span>';
        var cognatesList = [];
        try {
            var validJsonString = typeof v.cognates === 'string' ? v.cognates.replace(/'/g, '"') : JSON.stringify(v.cognates);
            cognatesList = JSON.parse(validJsonString);
        } catch (e) {
            console.error("Ошибка парсинга когнатов: ", e);
        }
        if (cognatesList && cognatesList.length > 0) {
            html += '  <div style="max-height: 350px; overflow-y: auto; overflow-x: auto; border: 1px solid #edf2f7; border-radius: 6px; background: #f8fafc;">';
            html += '    <table style="width: 100%; border-collapse: collapse; font-size: 13px; text-align: left; min-width: 800px;">';
            html += '      <thead style="position: sticky; top: 0; background: #2c3e50; color: #ffffff; z-index: 10;">';
            html += '        <tr>';
            html += '          <th style="padding: 10px 12px; font-weight: 600;">Реконструкция</th>';
            html += '          <th style="padding: 10px 12px; font-weight: 600;">Значение</th>';
            html += '        </tr>';
            html += '      </thead>';
            html += '      <tbody>';
            for (var j = 0; j < cognatesList.length; j++) {
                var item = cognatesList[j];
                var bg = j % 2 === 0 ? '#ffffff' : '#f1f5f9';
                html += '      <tr style="background: ' + bg + '; border-bottom: 1px solid #edf2f7;">';
                html += '        <td style="padding: 10px 12px; font-family: monospace; font-weight: bold; color: #c0392b;">' + (item.reconstruction || '—') + '</td>';
                html += '        <td style="padding: 10px 12px; color: #334155; font-style: italic;">' + (item.meaning || '—') + '</td>';
                html += '      </tr>';
            }
            html += '      </tbody>';
            html += '    </table>';
            html += '  </div>';
            html += '  <div style="font-size: 11px; color: #94a3b8; text-align: right; margin-top: 4px;">Всего вариантов: ' + cognatesList.length + '</div>';
        } else {
            html += '  <p style="color: #94a3b8; font-style: italic; font-size: 13px; margin: 0;">Когнаты отсутствуют или не распознаны.</p>';
        }
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
