function createPerson(name, age) {
 let _name = name;
    let _age = age;

    return {
        getName: function() {
            return _name;
        },
        getAge: function() {
            return _age;
        },
        setName: function(newName) {
            _name = newName;
        },
        setAge: function(newAge) {
            _age = newAge;
        }
    };
}