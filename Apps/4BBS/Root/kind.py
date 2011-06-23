#_*_ coding: utf-8 _*_

import sys
from quixote.directory import Directory
from Template import Template
from quixote import get_field,redirect
from Template import Template
from tools import *
from quixote import get_user, get_session, get_session_manager,get_response,get_cookie


class KindDirectory(Directory):
    _q_exports = ["","new","edit","delete","login","logout"]

    def _q_index(self):
        cookie = get_cookie('user')
        if cookie == 'Peter':
            this_session = get_session()
            this_session.set_user('Peter')
        if not get_user():
            body = Template.Kind_Body % (Template.Kind_Top,"Not Login!","")
            html = Template.HTML % ("Not login!",body)
            return html
        get_response().set_cookie('user','Peter',path='/',expires="Thu 01-Jan-2020 00:00:00 GMT")
        sql = """SELECT * FROM kind"""
        count,res = execute_sql_in_4bbs(sql,"SHOW")
        list = ""
        for e in res:
            list += "<div>"
            list += "Kind_id:<span>" + str(e[0]) + "</span><span>----</span>"
            list += "Kind_name:<span>" + str(e[1]) + "</span><span>----</span>"
            list += "Kind_count:<span>" + str(e[2]) + "</span><span>----</span>"
            list += "Kind_shortname:<span>" + str(e[3]) + "</span><span>----</span>"
            list += '<a href="/kind/delete?kind_id=' + str(e[0]) + '">Delete</a><span>----</span>'
            list += '<a href="/kind/edit?kind_id=' + str(e[0]) + '">Edit</a>'
            list += "</div>"
        body = Template.Kind_Body %(Template.Kind_Top,list,"")
        html = Template.HTML % ("Kind Index",body)
        return html 

    def new(self):
        """docstring for new"""
        if not get_user():
            body = Template.Kind_Body % (Template.Kind_Top,"Not Login!","")
            html = Template.HTML % ("Not login!",body)
            return html
        if get_field('action') != 'new':
            form = """
                   <form action="new" method="POST" accept-charset="utf-8">
                       <input type="hidden" name="action" value="new">
                       <div><input type="text" name="kind_name" value=""><span>Kind Name</span></div>
                       <div><input type="text" name="kind_shortname" value=""><span>Kind Short Name</span></div>
                   <p><input type="submit" value="新增"></p>
                   </form>
                   """
            body = Template.Kind_Body %(Template.Kind_Top,form,"")
            html = Template.HTML % ("New Kind",body)
            return html
        else:
            kind_name = get_field('kind_name')
            kind_shortname = get_field('kind_shortname')
            kind_id = int(get_time_str())
            kind_count = 0
            sql = """insert into kind values (%s,%s,%s,%s)"""
            execute_sql_in_4bbs(sql,[kind_id,kind_name,kind_count,kind_shortname])
            return redirect("/kind")
    
    def delete(self):
        if not get_user():
            body = Template.Kind_Body % (Template.Kind_Top,"Not Login!","")
            html = Template.HTML % ("Not login!",body)
            return html
        kind_id = get_field('kind_id')
        sql = """DELETE FROM kind where kind_id=%s"""
        execute_sql_in_4bbs(sql,[kind_id])
        return redirect("/kind")

    def edit(self):
        if not get_user():
            body = Template.Kind_Body % (Template.Kind_Top,"Not Login!","")
            html = Template.HTML % ("Not login!",body)
            return html
        
        if get_field('action') != 'edit':
            kind_id = get_field('kind_id')
            if not kind_id:
                Body = Template.Kind_Body % (Template.Kind_Top,"Error Parameters!","")
                return Template.HTML % ("Error!",Body)
            sql = """select * from kind where kind_id=%s""" % kind_id
            count,res = execute_sql_in_4bbs(sql,"SHOW")
            kind_name = res[0][1]
            kind_shortname= res[0][3]
            form = """
                    <form action="edit" method="POST" accept-charset="utf-8">
                       <input type="hidden" name="action" value="edit">
                       <div><input type="text" name="kind_name" value="%s"><span>Kind Name</span></div>
                       <div><input type="text" name="kind_shortname" value="%s"><span>Kind Short Name</span></div>
                       <input type="hidden" name="kind_id" value="%s">
                   <p><input type="submit" value="编辑"></p>
                   </form>
                   """ % (kind_name,kind_shortname,kind_id)
            body = Template.Kind_Body % (Template.Kind_Top,form,"")
            html = Template.HTML % ("Edit Kind",body)
            return html

        else:
            kind_id = int(get_field('kind_id'))
            kind_name = get_field('kind_name')
            kind_shortname = get_field('kind_shortname')
            sql = """UPDATE kind SET kind_name=%s,kind_shortname=%s where kind_id=%s"""
            execute_sql_in_4bbs(sql,[kind_name,kind_shortname,kind_id])
            return redirect("/kind")

            
    def login(self):
        if get_field('action') != 'login':
            form = """
                     <form action="login" method="POST" accept-charset="utf-8">
                       <input type="hidden" name="action" value="login">
                       <div><input type="text" name="name" value=""><span>Name</span></div>
                       <div><input type="text" name="password" value=""><span>Password</span></div>
                   <p><input type="submit" value="登陆"></p>
                   </form>
                   """
            body = Template.Kind_Body % (Template.Kind_Top,form,"")
            html = Template.HTML % ("Login",body)
            return html
        else:
            name = get_field('name')
            password = get_field('password')
            if name == 'Peter' and password == '112358132134art':
                this_session = get_session()
                this_session.set_user('Peter')
            return redirect('/kind')

    def logout(self):
        get_response().expire_cookie('user',path='/')
        get_session_manager().expire_session()
        body = Template.Kind_Body % (Template.Kind_Top,"Has logout!","")
        html = Template.HTML % ("Logout",body)
        return html

