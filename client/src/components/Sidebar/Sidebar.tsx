import { NavLink } from 'react-router-dom'
import styles from './Sidebar.module.css'

const links = [
  { to: '/operators', label: 'Operators', icon: '🧑‍💻' },
  { to: '/robots', label: 'Robots', icon: '🤖' },
  { to: '/stations', label: 'Stations', icon: '🏭' },
  { to: '/collection-items', label: 'Collection Items', icon: '📦' },
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
            <span>{link.icon}</span>
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