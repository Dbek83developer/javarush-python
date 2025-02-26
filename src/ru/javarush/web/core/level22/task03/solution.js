function performTask() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const randomNumber = Math.random();
      if (randomNumber > 0.5) {
        resolve("Task completed successfully");
      } else {
        reject("Task failed");
      }
    }, 2000);
  });
}

performTask()
  .then(message => {
    console.log(message);
  })
  .catch(error => {
    console.error(error);
  })
  .finally(() => {
    console.log("Task is completed");
  });