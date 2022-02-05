var memberArray = ['egoing', 'graphittie', 'leezhce']
console.group('array loop');
var i = 0;
while(i , i < memberArray.length){
    console.log(i, memberArray[i]);
    i++;
}
console.groupEnd('array loop');
var memberObject = {
    manager: 'egoing',
    developer:'graphittie',
    designer:'leezhce'
}

console.group('object loop');
for(var name in memberObject){
    console.log(name, memberObject[name]);
}
memberObject.designer = 'leezche';