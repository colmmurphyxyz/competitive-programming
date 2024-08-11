type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };

function argumentsLength(...args: JSONValue[]): number {
    let argsLength: number = 0;
    for (const arg of args) {
        argsLength++;
    }
    return argsLength
};