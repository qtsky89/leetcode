type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
    if (arr.length == 0) {
        return []
    }

    const ret = []

    let tmp = 0
    let tmpArray = []
    for(let i=0; i< arr.length;i++) {
        if (tmpArray.length == size) {
            ret.push(tmpArray)
            tmpArray = []
        }

        tmpArray.push(arr[i])
    }

    if (tmpArray) {
        ret.push(tmpArray)
    }


    return ret
};
