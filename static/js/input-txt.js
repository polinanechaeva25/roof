let inputs = document.querySelectorAll('.input__file');

Array.prototype.forEach.call(inputs, function (input) {
  let label = input.nextElementSibling,
    labelVal = label.querySelector('.input__file-button-text').innerText;

  input.addEventListener('change', function (e) {
    let countFiles = '';
    if (this.files && this.files.length >= 1)
      countFiles = this.files.length;

    if (countFiles > 1)
      label.querySelector('.input__file-button-text').innerText = 'Выберете только 1 файл! ';
    else if (countFiles == 1)
      label.querySelector('.input__file-button-text').innerText = 'Файл выбран: ' + e.target.value.split( '\\' ).pop();
    else
      label.querySelector('.input__file-button-text').innerText = labelVal;
  });
});

const file = document.getElementById('file')

file.addEventListener('change', (event) => {
  const target = event.target
  	if (target.files && target.files[0]) {

      /*Maximum allowed size in bytes
        20MB Example
        Change first operand(multiplier) for your needs*/
      const maxAllowedSize = 20 * 1024 * 1024;
      if (target.files[0].size > maxAllowedSize) {
      	// Here you can ask your users to load correct file
       	alert('Максимальный размер файла - это 20MB!')
       	target.value = ''
      }
  }
})