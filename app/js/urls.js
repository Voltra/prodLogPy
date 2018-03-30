export function assets(uri){
    return `/static/${uri}`;
}

export function json(uri){
    return assets(`json/${uri}`);
}