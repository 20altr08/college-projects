function highlight_navstuff() {
    let currentpage = document.title.split(' ')[0].toLowerCase()
    nav.querySelectorAll("a").forEach(a => {
        if (a.id === currentpage) {
            a.classList.add("active");
        }
    })
}
let nav = document.getElementById("navbar-links")