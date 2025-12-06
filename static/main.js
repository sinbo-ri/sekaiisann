let list = [];
let idx = 0;

function loadQuestions() {
    const subject = document.getElementById("subject").value;
    const start = document.getElementById("start").value;
    const end = document.getElementById("end").value;
    const mode = document.getElementById("mode").value;

    fetch(`/api/questions?subject=${subject}&start=${start}&end=${end}&mode=${mode}`)
        .then(r => r.json())
        .then(data => {
            list = data;
            idx = 0;
            show();
        });
}

function show() {
    if (list.length === 0) {
        alert("該当データがありません");
        return;
    }
    const q = list[idx];
    document.getElementById("unit").innerText = "【" + q.unit + "】";
    document.getElementById("question").innerText = q.question;
    document.getElementById("answer").classList.add("hidden");
    document.getElementById("answer").innerText = q.answer;
    document.getElementById("quiz").classList.remove("hidden");
}

function showAnswer() {
    document.getElementById("answer").classList.remove("hidden");
}

function next() {
    idx++;
    if (idx >= list.length) {
        alert("終了！");
        return;
    }
    show();
}
