import http from "k6/http";
import {check} from 'k6';

export const options = {
    vus: 2000,
    duration: '60s',
}

export default function () {
    let res = http.get('https://example.com/');
    check(res,{'status is 200': (res) => res.status === 200});
}