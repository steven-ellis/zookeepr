<table border="1">
<tr>
% for header in c.columns:
  <th><% header %></th>
% # endfor
</tr>

% rows = 0
% for row in c.data:
  <tr class="<% oddeven.next() %>">
%   rows += 1
%   for item in row:
      <td class="list">
%     try:
        <% item | h %>
%     except:
        <% `item` | h %>
%     #endtry
      </td>
%   # endfor
  </tr>
% # endfor
</table>
(<% rows |h%> rows)<br/>

<br><p class="note">
<% c.sql %>
</p>

<%init>
def oddeven():
  while 1:
    yield "odd"
    yield "even"
oddeven = oddeven()
</%init>
