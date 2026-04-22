import { useOperators } from "../hooks/useOperator";

export const OperatorPage = () => {
    const {operators, loading, error } = useOperators()
    if(loading) return <div> loading ... </div>
    if(error) return <div> error ...</div>
    return(
        <div>
            <h1>Operators </h1>
             <table>
                <thead>
                <tr>
                    <th>Number</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Active</th>
                </tr>
                </thead>
             </table>
             <tbody>
                {operators.map((op)=>(
                    <tr key = {op.id}>
                        <td>{op.operator_number}</td>
                        <td>{op.full_name}</td>
                        <td>{op.email}</td>
                        <td>{op.is_active ? 'YES' : 'No'}</td>
                    </tr>
                ))}
             </tbody>
        </div>
    )
}  