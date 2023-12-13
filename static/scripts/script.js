// Закрываем все вкладки сайдбара
const toggler = document.querySelector(".btn");
toggler.addEventListener("click", function () {
    document.querySelector("#sidebar").classList.toggle("collapsed");
});

// Скрипт установки таймера уведомления
// Показать уведомление при загрузке страницы, если оно есть
window.onload = function () {
    var notification = document.getElementById('notification');
    if (notification !== null && notification.innerText.trim() !== "") {
        notification.style.display = 'block';
        // Установить таймер на скрытие уведомления через 3 секунды (3000 миллисекунд)
        setTimeout(function () {
            notification.style.display = 'none';
        }, 3000);
    }
};

// Получаем коллекцию элементов по классу
const add_buttons = document.getElementsByClassName("add-button");
const edit_buttons = document.getElementsByClassName("edit-button");
const delete_buttons = document.getElementsByClassName("delete-button");
const filter_buttons = document.getElementsByClassName("filter-button");

let i;
// Проходимся по каждому элементу и добавляем атрибут title
for (i = 0; i < add_buttons.length; i++) {
    add_buttons[i].setAttribute("title", "Добавить запись");
}
for (i = 0; i < edit_buttons.length; i++) {
    edit_buttons[i].setAttribute("title", "Редактировать запись");
}
for (i = 0; i < delete_buttons.length; i++) {
    delete_buttons[i].setAttribute("title", "Удалить запись");
}
for (i = 0; i < filter_buttons.length; i++) {
    filter_buttons[i].setAttribute("title", "Фильтровать записи");
}