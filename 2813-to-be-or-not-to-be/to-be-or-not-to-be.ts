type ToBeOrNotToBe = {
    toBe: (val: any) => boolean;
    notToBe: (val: any) => boolean;
};

function expect(val: any): ToBeOrNotToBe {
    return {
        toBe: (val2: any): boolean => {
          if (val !== val2) {
            throw new Error("Not Equal")
          } else {
            return true
          }
        },
        notToBe: (val2: any): boolean => {
          if (val === val2) {
            throw new Error("Equal")
          } else {
            return true
          }
        },
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */