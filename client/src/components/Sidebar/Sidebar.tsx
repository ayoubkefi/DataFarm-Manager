import { NavLink } from 'react-router-dom'
import styles from './Sidebar.module.css'

const links = [
  { to: '/operators', label: 'Operators', image : './icons/Operators-sidebar.svg' },
  { to: '/robots', label: 'Robots', image : './icons/Robots-sidebar.svg' },
  { to: '/stations', label: 'Stations', image : './icons/Stations-sidebar.svg' },
  { to: '/Sops', label : 'Sops', image : './icons/Sops-sidebar.svg'},
  { to: '/collection-items', label: 'Collection Items', image : './icons/CollectionItems-sidebar.svg' },
  
]

export const Sidebar = () => {
  return (
    <div className={styles.sidebar}>
      <p className={styles.title}>DataFarm Manager</p>
      <nav className={styles.nav}>
        {links.map((link) => (
          <NavLink
            key={link.to}
            to={link.to}
            className={({ isActive }) =>
              isActive
                ? `${styles.link} ${styles.activeLink}`
                : styles.link
            }
          >
            <span><img src={link.image} alt={link.label} width={18} height={18}/></span>
            <span>{link.label}</span>
          </NavLink>
        ))}
      </nav>
      <div className={styles.bottom}>
        <img
          src="/agile-robots-logo.svg"
          alt="Agile Robots"
          className={styles.logoImage}
        />
      </div>
    </div>
  )
}