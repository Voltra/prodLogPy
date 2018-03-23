export default class TableGenerator{

    /**
     * Contructor of the class TableGenerator
     * @param {HTMLElement} elem - being the html on which we target the constructor and the load method.
     * @param {Array} data - being the data to be loaded in the table.
     */
    constructor(elem, data) {
        if (!(data instanceof Array))
            throw new TypeError("Data should be an array");

        const table = document.createElement("table");
        this.$elem = $(elem);
        this.$elem.append(table);
        this.$table = this.$elem.children("table");
        this.load(data);
    }

    load(data = []) {
        this.$elem.empty();
        this.$table.empty();
        this.$elem.append(this.$table);

        const head = document.createElement("tr");
        if(data.length === 0)
            return;

        const columnNames = Object.keys(data[0]);
        columnNames
        .map(columnName => {
            const th = document.createElement("TH");
            th.innerText = columnName;
            return th;
        }).forEach(::head.appendChild);

        data.forEach(elem => {
            const values = Object.entries(elem).map(([key, value]) => ({key, value}));

            values.sort((lhs, rhs) => {
                const indexOfLhs = columnNames.indexOf(lhs);
                const indexOfRhs = columnNames.indexOf(rhs);

                if(indexOfLhs < indexOfRhs)
                    return -1;
                else if(indexOfLhs > indexOfRhs)
                    return 1;
                else
                    return 0;
            });

            const tr = document.createElement("tr");
            values.map(elem => {
                const td = document.createElement("td");
                td.innerText = elem.value;
                return td;
            }).forEach(::tr.appendChild)
        })
    }
}