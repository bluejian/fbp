export const getImg = (path) => {
    if (!path) return '';
    const base = import.meta.env.BASE_URL || '/';
    if (path.startsWith('http') || path.startsWith('data:')) return path;

    if (path.startsWith('/')) {
        return base + path.slice(1);
    }
    return base + path;
};
