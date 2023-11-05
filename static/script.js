document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('symptom-form');
    const pointsList = document.getElementById('points-list');

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const symptom = document.getElementById('symptom').value;

        pointsList.innerHTML = '<p>Loading...</p>'; // ローディングメッセージを表示

        fetch(`/api/points?symptom=${encodeURIComponent(symptom)}`)
            .then(response => response.json())
            .then(data => {
                pointsList.innerHTML = ''; // ローディングメッセージをクリア
                data.forEach(point => {
                    const pointElement = document.createElement('p');
                    pointElement.innerText = `${point.name}: ${point.description}`;
                    pointsList.appendChild(pointElement);
                });
            })
            .catch(error => {
                pointsList.innerHTML = '<p>エラーが発生しました。</p>'; // エラーメッセージを表示
            });
    });
});
