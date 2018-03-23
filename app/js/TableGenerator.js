import utf8 from "fix-utf8"


export default class TableGenerator{
    /**
     * Constructor of the class TableGenerator
     * @param {HTMLElement|DOMString} elem - being the html on which we target the constructor and the load method.
     * @param {Array} data - being the data to be loaded in the table.
     */
    constructor(elem, data = []) {
        if (!(data instanceof Array))
            throw new TypeError("Data should be an array");

        const table = document.createElement("table");
        const ID = "table_generated_table";
        table.id = ID;
        this.$elem = $(elem);
        this.$elem.append(table);
        this.$table = $(table);
        this.load(data);
    }

    /**
     * Method generating the html from an array of data
     * @param {Array} data - being the data to be generating as a html table
     */
    load(data = []) {
        this.$elem.empty();
        this.$table.empty();
        console.log("table: ", this.$table);
        this.$elem.append(this.$table);

        const thead = document.createElement("thead");
        const head = document.createElement("tr");
        thead.appendChild(head);
        if(data.length === 0)
            return;

        const columnNames = Object.keys(data[0]);
        columnNames
        .map(columnName => {
            const th = document.createElement("th");
            th.innerText = utf8(columnName);
            return th;
        }).forEach(::head.appendChild);

        const tbody = document.createElement("tbody");
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
            values.map(_ => {
                const td = document.createElement("td");
                td.innerText = utf8(_.value);
                return td;
            }).forEach(::tr.appendChild);
			tbody.append(tr);
        });
        this.$table.append(thead);
        this.$table.append(tbody);
    }
}