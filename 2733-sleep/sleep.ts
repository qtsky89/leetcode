async function sleep(millis: number): Promise<void> {
    return new Promise<void> ((resolve, reject) => {
        try {
            setTimeout(resolve, millis);
        } catch (err) {
            reject(err);
        }
    }
    )
}


/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */