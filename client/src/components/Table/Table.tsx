
import styles from './Table.module.css'
interface TableProps{
    headers : string[]
    rows :  string[][]

}

export const Table = ({headers, rows }:TableProps) =>{
    return(
        <table className= {styles.table}>
            <thead>
                <tr>
                    {headers.map((h) =>(
                        <th key ={h}>{h}</th>
                    ))}
                </tr>
            </thead>
            <tbody>
                {rows.map((row,rowIndex) =>(
                    <tr key={rowIndex}>
                    {row.map((cell,  cellIndex)=>(
                        <td  key = {cellIndex}>{cell}</td>
                    ))}
                    </tr>
                ))}
            </tbody>

        </table>
    )
}