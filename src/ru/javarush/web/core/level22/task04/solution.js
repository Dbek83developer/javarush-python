function loadImage() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve('Image loaded');
    }, 1000);
  });
}

function loadData() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve('Data loaded');
    }, 2000);
  });
}

Promise.all([loadImage(), loadData()]).then((results) => {
  console.log('All resources loaded', results);
});