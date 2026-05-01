import styles from './Table.module.css'

interface TableProps {
  headers: string[]
  rows: string[][]
  onDelete?: (indices: number) => void
  onEdit?: (rowIndex : number) => void
}

export const Table = ({ headers, rows, onDelete, onEdit }: TableProps) => {


  return (
      <table className={styles.table}>
        <thead>
          <tr>
            {headers.map((h) => (
              <th key={h}>{h}</th>
            ))}
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((row, rowIndex) => (
            <tr  key={rowIndex}>
              {row.map((cell, cellIndex) => (
                <td key={cellIndex}>{cell}</td>
              ))}
              {(onEdit || onDelete) &&(
                <td className={styles.actionsCell}>
                  {onEdit && (
                    <button
                      className={styles.editButton}
                      onClick={() => onEdit(rowIndex)}
                    >
                      Edit
                    </button>
                  )}
                  {onDelete && (
                    <button
                      className={styles.deleteButton}
                      onClick={() => onDelete(rowIndex)}
                    >
                      Delete
                    </button>
                  )}

                </td>
              )}



            </tr>
          ))}
        </tbody>
      </table>
  )
}