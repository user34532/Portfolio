export const fetchUserAnalytics = () => {
    // Simulate an API that fetches user analytics
    return fetch('/api/user-analytics')
        .then(response => response.json())
        .then(data => data);
};