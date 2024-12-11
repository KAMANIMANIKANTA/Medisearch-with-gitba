document.getElementById('themeSwitcher').addEventListener('change', function() {
    if (this.checked) {
        document.body.style.backgroundColor = '#333';
        document.body.style.color = '#fff';
        document.querySelectorAll('.btn').forEach(btn => btn.style.color = '#fff');
        document.querySelectorAll('table th').forEach(th => th.style.backgroundColor = '#444');
    } else {
        document.body.style.backgroundColor = '#f9f9f9';
        document.body.style.color = '#333';
        document.querySelectorAll('.btn').forEach(btn => btn.style.color = '');
        document.querySelectorAll('table th').forEach(th => th.style.backgroundColor = '#007bff');
    }
});
