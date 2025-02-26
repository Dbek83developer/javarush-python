async function postData() {
  const url = 'https://jsonplaceholder.typicode.com/posts';
  const data = {
    title: 'foo',
    body: 'bar',
    userId: 1
  };

  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });

  const result = await response.json();
  console.log(result);
}

postData();