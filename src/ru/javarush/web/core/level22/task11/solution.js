async function createPost() {
    const url = 'https://jsonplaceholder.typicode.com/posts';
    const postData = {
        title: 'New Post',
        body: 'This is a new post',
        userId: 1
    };

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(postData)
        });

        if (!response.ok) {
            console.error('Failed to create post:', response.statusText);
            return;
        }

        const data = await response.json();
        console.log('Post created:', data);
    } catch (error) {
        console.error('Error:', error);
    }
}