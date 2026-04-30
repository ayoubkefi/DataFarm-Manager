import { useState } from "react"
import styles from './Modal.module.css'
interface Field{
    key : string 
    label : string 
    type : 'text' | 'email' | 'number' | 'boolean'
}
interface ModalProps{
    title : string 
    fields : Field[]
    onClose : () => void 
    onSubmit : (data : Record<string,string>) => void
}

export const Modal = ({title, fields, onClose, onSubmit}: ModalProps) => {
    
    const [form, setForm] = useState<Record<string,string>>(
        Object.fromEntries(fields.map(f => [f.key,'']))
    )

    const handleSubmit = () =>{
        onSubmit(form)
        onClose()
    }
    return (
    <>
      <div className={styles.overlay} onClick={onClose} />
      <div className={styles.modal}>
        <div className={styles.header}>
          <h2 className={styles.title}>{title}</h2>
          <button className={styles.closeButton} onClick={onClose}>✕</button>
        </div>
        <div className={styles.body}>
          {fields.map(field => (
            <div key={field.key} className={styles.fieldGroup}>
              {field.type !== 'boolean' && (
                <label className={styles.label}>{field.label}</label>
              )}
              {field.type == 'boolean' ? (
                <select
                  className={styles.input}
                  value =  {form[field.key]}
                  onChange={e => setForm({...form,[field.key] : e.target.value})}
                >
                  <option value="true">Active</option>
                  <option value  = "false">Inactive</option>
                </select>
              ) : ( 
              <input
                className={styles.input}
                type={field.type}
                placeholder={field.label}
                value={form[field.key]}
                onChange={e => setForm({ ...form, [field.key]: e.target.value })}
              />
              )}
            </div>
          ))}
        </div>
        <div className={styles.actions}>
          <button className={styles.cancelButton} onClick={onClose}>Cancel</button>
          <button className={styles.submitButton} onClick={handleSubmit}>Create</button>
        </div>
      </div>
    </>
  )
}