export const getUsers = async (page) => {
    const response = await fetch(`http://127.0.0.1:5000/api/users?page=${page}`);
    return response.json();
}