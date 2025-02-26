async function updatePost() {
    const url = 'https://jsonplaceholder.typicode.com/posts/1';
    const postData = {
        title: 'Updated Post',
        body: 'This post has been updated',
        userId: 1
    };

    try {
        const response = await fetch(url, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(postData)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const updatedPost = await response.json();
        console.log(updatedPost);
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

updatePost();