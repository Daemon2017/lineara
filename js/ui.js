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
        html += '  <h3 style="margin-top: 0; color: #d97706;">Вариант #' + v.stressed_syllable_number + '</h3>';

        html += '  <p>1) Ударение падает на слог: <b>' + v.stressed_syllable_number + '</b></p>';

        html += '  <p>2) Реконструкция в пре-ПИЕ: <code style="background: #f3e8ff; color: #6b21a8; padding: 2px 6px; font-weight: bold;">' + v.pre_pie_r + '</code></p>';

        html += '  <p>3) Реконструкция в ПГ: <code style="background: #e0f2fe; color: #0369a1; padding: 2px 6px; font-weight: bold;">R: ' + v.pg_r + '</code>';
        if (v.pg_l) {
            html += ' | <code style="background: #ecfeff; color: #0e7490; padding: 2px 6px; font-weight: bold;">L: ' + v.pg_l + '</code>';
        }
        html += '  </p>';

        html += '  <p>4) Реконструкция в ПИЕ: <code style="background: #dcfce7; color: #15803d; padding: 2px 6px; font-weight: bold;">R: ' + v.pie_r + '</code>';
        if (v.pie_l) {
            html += ' | <code style="background: #ccfbf1; color: #0f766e; padding: 2px 6px; font-weight: bold;">L: ' + v.pie_l + '</code>';
        }
        html += '  </p>';

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
